import time
import threading
import numpy as np
import pygame
from dlpc4710.cypress import * 
from dlpc4710.dlpc347x_dual import *
 
class Projector:
    def __init__(self):
        """
        Initialize the projector using the Micro-Manager Core.
        Also, set up parameters for pulsed light control.
        """
        #### MODIFIED: Attributes for pulsed light control
        self.pulse_thread = None
        self._pulse_stop_event = threading.Event()
        self._pulse_run_event = threading.Event()
        self.other_event=None
        # Default pulsed light parameters:
        self.height=1080
        self.width=1920
        self.pulse_period = 3        # seconds
        self.pulse_dutyCycle = 5     # percent
        self.current_red = 100
        self.current_green = 100
        self.current_blue = 100
        self.other_time=None
        self.my_time=None
        self.flag=4
        self.counter=0
        self.metadata= None

    

    # ### MODIFIED: Consolidated pulsed light control into the Projector class.
    def _projecting(self):

        data=np.load(self.metadata, allow_pickle=True)
        keys=data.files
        arrays=[data[key] for key in keys]
        pattern_list=[tuple(items) for items in zip(*arrays)]

        with Cypress(0x36) as dev, LightCrafterDisplay(dev) as lcd:
        
            def WriteCommand (writebytes, protocoldata):
                # print ("writebytes ", [hex(x) for x in writebytes])
                dev.write(writebytes)

            def ReadCommand(readbytecount, writebytes, protocoldata):
                # print ("writebytes ", [hex(x) for x in writebytes])
                readbytes = dev.read(readbytecount, writebytes)
                # print ("readbytes ", [hex(x) for x in readbytes])
                return readbytes
            
            DLPC347X_DUALinit(ReadCommand, WriteCommand)
            WriteOperatingModeSelect(OperatingMode.ExternalVideoPort)
            time_zero=time.time()
            for  imagepattern,rC,gC,bC,pP,dU,dC,iS,*_ in pattern_list:
                # Parameter settings
                height,width = tuple(iS) # Image size std 800,1280
                WriteRgbLedCurrent(rC,gC,bC)
                onTime = pP * (dC/100.0)
                # Initialize Pygame
                pygame.init()

                # Set up display size
                screen_width = width
                screen_height = height

                # Get the number of screens
                num_screens = pygame.display.get_num_displays()
                # Get the position of the third screen
                if num_screens >=3:
                    screen=pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN,display=2)
                else:
                    print("Third screen not found.")
                    sys.exit()

                # Convert grayscale to RGB for Pygame compatibility
                pattern_rgb = np.stack([imagepattern]*3, axis=-1)  # Convert grayscale to RGB by stacking 3 channels

                # Convert the array to a surface for Pygame
                image_surface = pygame.surfarray.make_surface(pattern_rgb)

                # Display the image in full screen
                screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
                screen.blit(image_surface, (0, 0))

                # Show the image
                pygame.display.flip()
    
                t_start=time.time()
                t_current=t_start
                while(t_current-t_start<dU and not self._pulse_stop_event.is_set()):
                    self._pulse_run_event.wait()
                    WriteRgbLedEnable(False,False,True)
                    time.sleep(onTime)
                    WriteRgbLedEnable(False,False,False)
                    time.sleep(onTime)
                    self.counter+=1
                    t_current=time.time()
                    self._pulse_run_event.clear()
                    self.other_event.set()
                    # while(time.time()-t_current<=onTime):
                    #     WriteRgbLedEnable(False,False,True)
                    # print("Light")
                    # while(time.time()-t_current<=pP):
                    #     WriteRgbLedEnable(False,False,False)
            
                    # self.counter+=1
                    # t_current=time.time()
                    # # self._pulse_run_event.clear()
                    # # self.other_event.set()
                    # if self.counter>=self.flag:
                    #     self.counter=0
                    #     self.my_time=time.time()
                    #     if self.my_time-self.other_time<15:
                    #         time.sleep(self.looptime-self.my_time)
                    #         # print(time.time()-initial_time)
                    #     self._pulse_run_event.clear()
                    #     self.other_event.set()
                        
                pygame.quit()
                print("Time passed : ", t_current-t_start)
                print(rf"")
            WriteRgbLedEnable(False,False,False)

        return 1

       
    def start_pulsed_mode(self,metadata,other_event,other_time):
        """
        Start pulsed light control in a separate thread.
        Optional parameters can override defaults.
        """
        if metadata is not None:
            self.metadata = metadata
        if other_event is not None:
            self.other_event = other_event
        if other_time is not None:
            self.other_time = other_time
        self._pulse_run_event.clear()
        self._pulse_stop_event.clear()
        self.pulse_thread = threading.Thread(target=self._projecting)
        self.pulse_thread.start()

    def stop_pulsed_mode(self):
        """
        Stop the pulsed light control.
        """
        if self.pulse_thread is not None:
            self._pulse_stop_event.set()
            self.pulse_thread.join()
            self.pulse_thread = None
            
        

