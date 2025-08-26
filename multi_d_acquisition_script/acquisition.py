from Logger import *
from Camera import *
from Stage import *
import threading

class Acquisition:
    def __init__(self, core, image_folder = "", save_prefix="image_"):
        """
        Initialize the camera with a Micro-Manager Core instance and a folder for saving images.
        """
        self.core = core
        self.timestep= 1
        self.logger=None
        self.num_of_acq=None
        self.positions=None
        self.acquisition_thread = None
        self._acquisition_event = threading.Event()
        self._stop_acquisition_event = threading.Event()
        self.other_time=None
        self.my_time=0
        self.other_event=None

    def _acquisition(self):
        stage=Stage(self.core)
        camera=Camera(self.core)
        positions_xyz=stage.unpack_position(self.positions)
        for _ in range(self.num_of_acq):
            # self._acquisition_event.wait()
            # self.my_time=time.time()
            for flag,pos in enumerate(positions_xyz):
                X,Y,Z=pos
                start = time.perf_counter()
                stage.move_stage(X,Y,Z)
                camera.acquire(self.logger,self.timestep,flag)
                # print(start-time.perf_counter())
                self._acquisition_event.clear()
                self.other_event.set()
                self._acquisition_event.wait()
            camera.increase_daq_counter()
            # self._acquisition_event.clear()
            # self.other_event.set()

    
    def start_acquisition(self,num_of_acq,pos_file,time_step,logger,other_event):
        if num_of_acq is not None:
            self.num_of_acq=num_of_acq
        if pos_file is not None:
            self.positions=pos_file
        if time_step is not None:
            self.timestep=time_step
        if logger is not None:
            self.logger=logger
        if other_event is not None:
            self.other_event = other_event
        
        self._acquisition_event.set()
        self.acquisition_thread = threading.Thread(target=self._acquisition)
        self.acquisition_thread.start()
        
    
    def stop_acquisition(self):
        if self.acquisition_thread is not None:
            self._acquisition_event.set()
            self.acquisition_thread.join()
            self.acquisition_thread = None
