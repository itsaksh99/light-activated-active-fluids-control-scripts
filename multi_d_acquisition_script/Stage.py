from pycromanager import JavaObject
import time 
class Stage:
    def __init__(self, core):
        """
        Initialize the camera with a Micro-Manager Core instance and a folder for saving images.
        """
        self.core = core
        self.daq_counter = 0

    def unpack_position(self,pos_filepath):
        positionList = JavaObject('org.micromanager.PositionList')
        positionList.load(pos_filepath) # Reads the .pos file
        num_positions = positionList.get_number_of_positions()
        positions = [positionList.get_position(i) for i in range(num_positions)]
        positions_xyz=[(position.get_x(),position.get_y(),position.get_z()) for position in positions]
        return positions_xyz
    
    def move_stage(self,x, y, z):
        self.core.set_xy_position(x, y)
        self.core.set_position('TIZDrive', z)
        
        self.core.wait_for_device('TIXYDrive')
        self.core.wait_for_device('TIZDrive')
        
        return 0