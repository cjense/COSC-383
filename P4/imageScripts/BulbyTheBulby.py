from sys import path
path.append('C:/Users/clair/Desktop/Coding/COSC-383/P4/')
import utils
import imageio.v3 as iio
import decode_image as di
import numpy as np
from PIL import Image as im

def decode_img(filename, savename):
    """Read an encoded image from a given image file"""
    # Load image
    img = iio.imread(filename)
    # Extract least-significant bits as string
    bits = utils.get_bits(img, lambda x: x&1)  # lambda gets LSB of x
    # Parse header
    height_bitstring = bits[0:32]
    width_bitstring = bits[32:64]
    height = int(height_bitstring, 2)
    width = int(width_bitstring, 2)
    print('Height: {}, width: {}'.format(utils.big_endian(height_bitstring), utils.big_endian(width_bitstring)))
    # Get image vals from bits after header
    img = bits_to_img(bits[64:], height, width)
    img.show()

def bits_to_img(bits, height, width):
    """Given a bitstring and dimensions for a desired image, read the bits as
    the channel values for a PIL Image object
    
    @param bits: a bitstring expected to have at least 8*height*width*3 bits,
        representing the values for the image in left-to-right, top-to-bottom,
        RGB order
    @param height: height of the desired image
    @param width: width of the desired image
    @return: a PIL Image object constructed from the parameters"""
    # Create an array of zeroes in the desired final shape
    array = np.zeros((height, width, 3), np.uint8)
    # Convert bits to bytes
    bytes = utils.bits_to_bytes(bits)
    i=0  # Counter for which byte we're working with
    # Iterate across channels, columns, rows to insert bytes appropriately
    for h in range(height):
        for w in range(width):
            for x in range(4):
                array[h, w, x] = int(bytes[i], 2)
                i += 1
    # Create image from array
    img = im.fromarray(array, mode='RGB')
    return img

decode_img('../PNGs/BulbyTheBulby.png', 'nosavename')