import os
import csv
import numpy as np
import tifffile
from patterngenerator import * # type: ignore

class lightpatterns:
    def __init__(self):
        self.imagesize=(1080,1920)
        self.pulse_period = 3        # seconds
        self.pulse_dutyCycle = 5     # percent
        self.redCurrent = 100
        self.greenCurrent = 100
        self.blueCurrent = 100
        self.pattern_type = 0
        self.pattern_parameters = 0
        self.bright=0
        self.dark=None
        self.duration=None
        self.logger=None
        return None
    
    def patterunpacker(self):
        height,width=self.imagesize
        if self.pattern_type==0:
            pattern=create_uniform_pattern(width,height,self.pattern_parameters, self.bright,self.dark) # type: ignore
            pattern_masked=pattern
        elif self.pattern_type==1:
            pattern = create_checkerboard_pattern(width, height, self.pattern_parameters, self.bright,self.dark) # type: ignore
        elif self.pattern_type==2:    
            pattern = create_half_brightness_pattern(width, height, self.pattern_parameters, self.bright,self.dark)# type: ignore
        elif self.pattern_type==3:
            pattern = create_stripe_pattern(width, height, self.pattern_parameters, self.bright,self.dark)# type: ignore
        elif self.pattern_type==4:
            pattern_masked=create_sine_pattern(width,height,self.pattern_parameters, self.bright,self.dark)# type: ignore
            # row1=865
            # row2=935
            # col1=390
            # col2=630
            # pattern_masked=np.zeros((width,height), dtype=np.uint8)
            # pattern_masked[row1:row2,col1:col2]=pattern[row1:row2,col1:col2]
        else:
            print("Not a valid pattern")
            pattern = np.zeros((width,height), dtype=np.uint8)
        
        
        return pattern_masked

    def make_profiles(self):
        experiment=[]
        image=self.patterunpacker()
        experiment.append((image,self.redCurrent,self.greenCurrent,self.blueCurrent,self.pulse_period,self.duration,self.pulse_dutyCycle,
                                   self.imagesize,self.bright,self.dark,self.pattern_type,self.pattern_parameters))
        return experiment

    def updateself(self,input):
        profiles=[]
        for rC,gC,bC,pP,dU,dC,bR,dA,pT,pA in input:
            self.pulse_period = pP        # seconds
            self.pulse_dutyCycle = dC     # percent
            self.redCurrent = rC
            self.greenCurrent = gC
            self.blueCurrent = bC
            self.pattern_type = pT
            self.pattern_parameters = pA
            self.bright= bR
            self.dark = dA
            self.duration = dU
            profiles.append(self.make_profiles()[0])
        return profiles
    
    def metadata(self,input,logger):
        parameters=self.updateself(input)

        self.logger=logger
        experiment_folder=logger.experiment_folder
        save_folder = os.path.join(experiment_folder)
        os.makedirs(save_folder, exist_ok=True)
        filename = os.path.join(save_folder,"patterns.csv")
        filename_npz = os.path.join(save_folder,"patterns.npz")
        
        
        
        with open(filename,'w',newline='') as file:
            df=csv.writer(file)
            df.writerow(["image_array","redCurrent","greenCurrent","blueCurrent","period(sec)","duration(sec)","duty_cycle","Height, Width","Maximum","Minimum","Pattern_type","Pattern_parameters"])
            for i in range(len(parameters)): 
                df.writerow([*parameters[i]])
                tifffile.imwrite(save_folder+rf"\pattern"+str(i)+".tif", parameters[i][0].T)
            file.close()
        
        keys=["image_array","redCurrent","greenCurrent","blueCurrent","period(sec)","duration(sec)","duty_cycle","Height, Width","Maximum","Minimum","Pattern_type","Pattern_parameters"]
        metadata_dict=[dict(zip(keys,value)) for value in parameters] 
        metadata=[]
        for i in keys:
            metadata.append([data[i] for data in metadata_dict])
        np.savez_compressed(filename_npz,images=metadata[0],redCurrent=metadata[1],greenCurrent=metadata[2],blueCurrent=metadata[3],
                            period=metadata[4],duration=metadata[5],duty_cycle=metadata[6],Imagesize=metadata[7],
                            Maximum=metadata[8],Minimum=metadata[9],Pattern_type=metadata[10],Pattern_parameters=metadata[11])
        
        # data=np.load(filename_npz, allow_pickle=True)
        # keys=data.files
        # # print(keys)
        # arrays=[data[key] for key in keys]
        # # print(arrays)
        # pattern_list=[tuple(items) for items in zip(*arrays)]
        # print(pattern_list)