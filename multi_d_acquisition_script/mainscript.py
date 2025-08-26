from pycromanager import Acquisition, Core
import numpy as np
import time
import argparse
import subprocess
import tkinter as tk
from Logger import *
from acquisition import * # type: ignore
from Projector_dlpc4710 import *
from profilegenerator import * # type: ignore

def create_parser():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--mode', choices=['init','patterns','experiment'], required=True,
                        help="Run initialization ('init') or acquisition ('acquire') mode.")
    
    parser.add_argument('--save_path', help="Local path to save the results", default='./nematics')

    # parser.add_argument('--config_filepath', help="Pycromanager config file path", default=r"C:\Program Files\Micro-Manager-2.0\Nikon_Zyla_SLM_SOLA.cfg")
    parser.add_argument('--config_filepath', help="Pycromanager config file path", default=r"C:\Program Files\Micro-Manager-2.0\katsu_zyla_nikonti_lumencor.cfg")

    return parser

# ------------------------------ Main Function ------------------------------
def main():
    global root_folder,logger,initial_time
    root_folder="D:\\Akshit"
    

    parser = create_parser()
    args = parser.parse_args()

    if args.mode == "init":
        mm_executable = r"C:\Program Files\Micro-Manager-2.0\ImageJ.exe"
        working_directory = r"C:\Program Files\Micro-Manager-2.0"

        waiting_time = 20
        print("Starting Micro-Manager...")

        subprocess.Popen([mm_executable, "--config", args.config_filepath], cwd=working_directory)
        time.sleep(waiting_time)

        core = Core()
        print("Loading configuration file...")
        core.load_system_configuration(args.config_filepath)
        time.sleep(waiting_time)

        core.set_config("Initialize", "On")
        print("Initialization complete. Instruments are configured for the day.")


    elif args.mode == 'patterns':
        logger = Logger(root_folder=root_folder)
        profile=lightpatterns() # type: ignore
        #(self.redCurrent,self.greenCurrent,self.blueCurrent,self.pulse_period,self.duration,self.pulse_dutyCycle,
        # self.bright,self.dark,self.pattern_type,self.pattern_parameters)
        # profile.metadata([(100,100,100,3,600,7,None,None,0,250),(100,100,100,3,300,7,None,None,0,0),(100,100,100,3,300,7,None,None,0,50),
        #                   (100,100,100,3,300,7,None,None,0,0),(100,100,100,3,300,7,None,None,0,100),(100,100,100,3,300,7,None,None,0,0),(100,100,100,3,300,7,None,None,0,150),
        #                   (100,100,100,3,300,7,None,None,0,0),(100,100,100,3,300,7,None,None,0,200),(100,100,100,3,300,7,None,None,0,0)],logger)
        profile.metadata([(100,100,100,3,300,7,None,None,0,250),(100,100,100,3,15000,7,200,20,4,50)],logger)
        

    elif args.mode == 'experiment':

        pos_filepath=r"D:\Akshit\20250731\xyz.pos"
        pattern_folder=r"D:\Akshit\20250731\experiment_9\patterns.npz"
        logger = Logger(root_folder=root_folder)
        core = Core()
        initial_time=time.time()
        projector=Projector()
        acquisition=Acquisition(core)
        # logger = Logger(root_folder=root_folder)
        projector.start_pulsed_mode(metadata=pattern_folder,other_event=acquisition._acquisition_event,other_time=acquisition.my_time)
        acquisition.start_acquisition(num_of_acq=3600,pos_file=pos_filepath,time_step=1,logger=logger,other_event=projector._pulse_run_event)
        acquisition.stop_acquisition()
        projector.stop_pulsed_mode()
        print("Experiment successful")


if __name__ == "__main__":
    main()

# config_names = core.get_available_config_groups()
# config_names_array = [config_names.get(i) for i in range(config_names.size())]
# loaded_devices_names = core.get_loaded_devices()
# loaded_devices_names_array = [loaded_devices_names.get(i) for i in range(loaded_devices_names.size())]
# print(config_names_array,loaded_devices_names_array)

# elif args.mode == 'experiment':
#     pos_filepath=r"D:\Akshit\20250624\xyz.pos"
#     root_folder="D:\\Akshit"
#     core = Core()
#     projector=Projector()
#     stage=Stage(core)
#     camera=Camera(core)
#     logger = Logger(root_folder=root_folder)
    
#     positions_xyz=stage.unpack_position(pos_filepath)    
#     timestep=1

#     projector.start_pulsed_mode(metadata=r"D:\Akshit\20250625\experiment_17\experiment.npz")
#     for _ in range(30):
#         for flag,pos in enumerate(positions_xyz):
#             X,Y,Z=pos
#             stage.move_stage(X,Y,Z)
#             camera.acquire(timestep,logger,flag)
#         camera.increase_daq_counter()
#     projector.stop_pulsed_mode()
