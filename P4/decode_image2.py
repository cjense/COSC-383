import sys

import imageio.v3 as iio
import numpy as np
from PIL import Image as im

import utils

def reverse(s):
    reversed = ''
    for i in range(len(s)):
        reversed = s[i]+reversed
    return reversed

def bits_to_img(bits, height, width, order='LRTB', colors='RGB'):
    """Given a bitstring and dimensions for a desired image, read the bits as
    the channel values for a PIL Image object
    
    @param bits: a bitstring expected to have at least 8*height*width*3 bits,
        representing the values for the image in left-to-right, top-to-bottom,
        RGB order
    @param height: height of the desired image
    @param width: width of the desired image
    @param order: are bits in order of LRTB or TBLR
    @return: a PIL Image object constructed from the parameters"""

    # Convert bits to bytes
    bytes = utils.bits_to_bytes(bits)
    reversed = []
    for b in bytes:
        reversed.append(reverse(b))
    bytes = reversed
    i=0  # Counter for which byte we're working with
    # Create an array of zeroes in the desired final shape
    array = np.zeros((height, width, 3), np.uint8)
    # Multiplier for color order
    color_order = 1 if colors == 'RGB' else -1

    if order == 'LRTB':
        # Iterate across channels, columns, rows to insert bytes
        for h in range(height):
            for w in range(width):
                for x in range(3):
                    array[h, w, (x*color_order)] = int(bytes[i], 2)
                    i += 1

    if order == 'TBLR':
        # Iterate across channels, rows, columns to insert bytes
        for w in range(width):
            for h in range(height):
                for x in range(3):
                    array[h, w, (x*color_order)] = int(bytes[i], 2)
                    i += 1

    # Create image from array
    img = im.fromarray(array, mode='RGB')
    return img



def img_to_bytes(img):
    png_encoded = iio.imwrite("<bytes>", img, extension=".png")
    return png_encoded


def default_decode_img(filename):
    """Read an encoded image from a given image file
    LRTB, 3x32b little-endian header, RGB, LSB"""
    # Load image
    img = iio.imread(filename)
    # Extract least-significant bits as string
    bits = utils.get_bits2(img)
    # Parse header
    height_bitstring = bits[0:32]
    width_bitstring = bits[32:64]
    height = int(height_bitstring, 2)
    width = int(width_bitstring, 2)
    print('Height: {}, width: {}'.format(height, width))
    # Get image vals from bits after header
    img = bits_to_img(bits[64:], height, width)
    return img


if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = 'hide_image.png'
    default_decode_img(target).show()