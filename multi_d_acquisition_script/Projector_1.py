import time
import threading
import numpy as np

class Projector:
    def __init__(self, core):
        """
        Initialize the projector using the Micro-Manager Core.
        Also, set up parameters for pulsed light control.
        """
        self.core = core
        self.slm_name = self.core.get_slm_device()
        self.width = self.core.get_slm_width(self.slm_name)
        self.height = self.core.get_slm_height(self.slm_name)
        self.current_intensity = None
        # Continuous mode: Initialize with a chosen intensity (e.g., 120)
        self.set_intensity(0)
        
        # ### MODIFIED: Attributes for pulsed light control
        self.pulse_thread = None
        self._pulse_stop_event = threading.Event()
        # Default pulsed light parameters:
        self.pulse_period = 3        # seconds
        self.pulse_dutyCycle = 5     # percent
        self.current_red = 0
        self.current_green = 0
        self.current_blue = 65

    def set_intensity(self, intensity):
        """
        Set the SLM intensity.
        Args:
            intensity (float): A value between 0 and 255.
        """
        self.current_intensity = intensity
        slm_image = self.current_intensity * np.ones([self.height, self.width], dtype='uint8')
        slm_image = np.clip(slm_image, 0, 255)
        self.core.set_slm_image(self.slm_name, slm_image.flatten())
        self.core.display_slm_image(self.slm_name)


    # ### MODIFIED: Consolidated pulsed light control into the Projector class.
    def _pulsed_light_loop(self):
        """
        Internal method that runs in a thread to control pulsed light using LCR4500.
        It uses pycrafter4500 and sends USB commands to pulse the blue LED.
        """
        import pycrafter4500
        from pycrafter4500 import connect_usb
        
        # Initialize LCR4500
        pycrafter4500.power_up()
        pycrafter4500.video_mode()
        
        # Disable all LEDs initially
        with connect_usb() as lcr:
            lcr.command('w', 0x00, 0x1A, 0x07, [int('00000000', 2)])
        
        # Set LED PWM polarity (inverted)
        with connect_usb() as lcr:
            lcr.command('w', 0x00, 0x1A, 0x05, [1])
        
        # Set LED currents (Red, Green, Blue)
        with connect_usb() as lcr:
            lcr.command('w', 0x00, 0x0B, 0x01, [self.current_red, self.current_green, self.current_blue])
        
        onTime = self.pulse_period * (self.pulse_dutyCycle / 100.0)
        offTime = self.pulse_period - onTime
        
        print(f"Pulsed light control started: period={self.pulse_period}s, dutyCycle={self.pulse_dutyCycle}%")
        print(self.height,self.width,self.current_blue,self.pulse_period)
        while not self._pulse_stop_event.is_set():
            # Enable blue LED (bit 2 set to 1)
            with connect_usb() as lcr:
                lcr.command('w', 0x00, 0x1A, 0x07, [int('00000100', 2)])
            time.sleep(onTime)
            if self._pulse_stop_event.is_set():
                break
            # Disable all LEDs
            with connect_usb() as lcr:
                lcr.command('w', 0x00, 0x1A, 0x07, [int('00000000', 2)])
            time.sleep(offTime)
        print("Pulsed light control stopped.")
        
        with connect_usb() as lcr:
            lcr.command('w', 0x00, 0x1A, 0x07, [int('00000000', 2)])
            pycrafter4500.power_down()


    def start_pulsed_mode(self, period=None, dutyCycle=None, current_red=None, current_green=None, current_blue=None):
        """
        Start pulsed light control in a separate thread.
        Optional parameters can override defaults.
        """
        if period is not None:
            self.pulse_period = period
        if dutyCycle is not None:
            self.pulse_dutyCycle = dutyCycle
        if current_red is not None:
            self.current_red = current_red
        if current_green is not None:
            self.current_green = current_green
        if current_blue is not None:
            self.current_blue = current_blue
        
        self._pulse_stop_event.clear()
        self.pulse_thread = threading.Thread(target=self._pulsed_light_loop)
        self.pulse_thread.start()

    def stop_pulsed_mode(self):
        """
        Stop the pulsed light control.
        """
        if self.pulse_thread is not None:
            self._pulse_stop_event.set()
            self.pulse_thread.join()
            self.pulse_thread = None
            
        

