import tifffile
from pycromanager import Studio
import numpy as np
import os
import time

class Camera:
    def __init__(self, core, image_folder = "", save_prefix="image_"):
        """
        Initialize the camera with a Micro-Manager Core instance and a folder for saving images.
        """
        self.core = core
        self.timestep= 1
        self.logger=None
        self.daq_counter = 0 

    def capture_image(self, show=True):
        """
        Capture an image using either Studio’s snap command or Core’s snap_image.
        Returns:
            image (np.ndarray): 2D numpy array (uint16) of the captured image.
        """
        if show:
            tagged_image = Studio().get_snap_live_manager().snap(True).get(0).legacy_to_tagged_image()
        else:
            self.core.snap_image()
            tagged_image = self.core.get_tagged_image()
        image = np.reshape(tagged_image.pix, newshape=[tagged_image.tags['Height'],tagged_image.tags['Width']])
        return image.astype(np.uint16)

    def save_image(self, image, filename):
        """
        Save the given image to disk.
        """
        tifffile.imwrite(filename, image, photometric='minisblack')


    def acquire(self,logger,timestep,flag=1):
        self.logger=logger
        self.timestep= timestep
        experiment_folder = logger.experiment_folder
        image_folder = os.path.join(experiment_folder, "image",str(flag))
        os.makedirs(image_folder, exist_ok=True)
        count = self.daq_counter
        save_prefix = rf"image_{logger.date}_{logger.experiment_number}_"+str(flag)+"_"

        # --- Step 1: Capture and Save Two Images ---
        image_A = self.capture_image(show=True)
        time.sleep(timestep)
        image_B = self.capture_image(show=True)
        filename_A = os.path.join(image_folder, f"{save_prefix}{count}_0.tif")
        self.save_image(image_A, filename_A)
        filename_B = os.path.join(image_folder, f"{save_prefix}{count}_1.tif")
        self.save_image(image_B, filename_B)
        return 0
    
    def increase_daq_counter(self):
        self.daq_counter+=1

    def reset_daq_counter(self):
        self.daq_counter = 0
    

