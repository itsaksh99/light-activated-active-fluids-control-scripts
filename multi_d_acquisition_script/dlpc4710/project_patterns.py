import numpy as np
import pygame
import sys
import time
from cypress import *
from dlpc347x_dual import *


def projecting(filename):
    
    data=np.load(filename, allow_pickle=True)
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
            while(t_current-t_start<dU):
                while(time.time()-t_current<=onTime):
                    WriteRgbLedEnable(True,True,True)
                while(time.time()-t_current<=pP):
                    WriteRgbLedEnable(False,False,False)
                t_current=time.time()
            
            pygame.quit()
            print("Time passed : ", t_current-t_start)
            print(rf"")
        WriteRgbLedEnable(False,False,False)
    return 1

# projecting(r"D:\Akshit\20250625\experiment_18\experiment.npz")