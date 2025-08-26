import numpy as np

def create_uniform_pattern(width, height, brightness,_,dark):
    """ Creates a pattern with uniform brightness"""
    pattern = brightness*np.ones((width,height), dtype=np.uint8)
    return pattern

def create_stripe_pattern(width, height, stripe_width, brightness_bright, brightness_dark):
    """ Creates a stripe pattern """
    pattern = np.zeros((width,height), dtype=np.uint8)
    for y in range(height):
        for x in range(width):
            if (x // stripe_width) % 2 == 0:
                pattern[x,y] = brightness_bright
            else:
                pattern[x,y] = brightness_dark
    return pattern

def create_checkerboard_pattern(width, height, checkerboard_size, brightness_bright, brightness_dark):
    """ Creates a checkerboard pattern"""
    pattern = np.zeros((width,height), dtype=np.uint8)
    for y in range(height):
        for x in range(width):
            if ((x // checkerboard_size) + (y // checkerboard_size)) % 2 == 0:
                pattern[y, x] = brightness_bright
            else:
                pattern[y, x] = brightness_dark
    return pattern

def create_gradient_pattern(width, height, brightness_bright):
    """ Creates a gradation pattern """
    pattern = np.zeros((width,height), dtype=np.uint8)
    for y in range(height):
        pattern[y, :] = np.linspace(0, brightness_bright, width, dtype=np.uint8)
    return pattern

def create_half_brightness_pattern(width, height, boundary_position, brightness_top, brightness_bottom):
    """ Creates a pattern with different brightness for the top and bottom halves """
    pattern = np.zeros((width,height), dtype=np.uint8)
    boundary = int(width * boundary_position)  # Convert boundary position to pixels
    for x in range(width):
        if x < boundary:
            pattern[:, x] = brightness_top  # Top half
        else:
            pattern[:, x] = brightness_bottom  # Bottom half
    return pattern

def create_sine_pattern(width, height, frequency, brightness_top, brightness_bottom):
    """ Creates a pattern with sinusoidal intensity profile """
    offset=(brightness_bottom+brightness_top)/2
    amplitude=(brightness_top-brightness_bottom)/2
    pattern = np.zeros((width,height), dtype=np.uint8)
    for x in range(height):
        pattern[:,x] = amplitude*np.sin(2*np.pi*frequency*x/height) +offset
    return pattern