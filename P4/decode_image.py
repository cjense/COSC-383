import sys

import imageio.v3 as iio
import numpy as np
from PIL import Image as im

import utils

'''Don't think we need this for now, it's just getting the dimensions of the original image, not
necessarily the hidden one'''
# function to extract 64-bit header, height, and width
def get_hw(img):
    height, width, _ = img.shape
    print("Height:", height, "Width:", width)
    return [height, width]


def bits_to_img(bits, height, width):
    """Given a bitstring and dimensions for a desired image, read the bits as the channel
    values for a PIL Image object"""
    # Create an array of zeroes in the desired final shape
    array = np.zeros((height, width, 3), np.uint8)
    # Convert bits to bytes
    bytes = utils.bits_to_bytes(bits)
    i=0  # Counter for which byte we're working with
    # Iterate across channels, columns, rows to insert bytes appropriately
    for h in range(height):
        for w in range(width):
            for x in range(3):
                array[h, w, x] = int(bytes[i], 2)
                i += 1
    # Create image from array
    img = im.fromarray(array, mode='RGB')
    return img


def img_to_bytes(img):
    png_encoded = iio.imwrite("<bytes>", img, extension=".png")
    return png_encoded


def decode_img(filename):
    """Read an encoded image from a given image file"""
    # Load image
    img = iio.imread(filename)
    # Extract least-significant bits as string
    bits = utils.get_bits(img, 1)
    # Parse header
    height_bitstring = bits[0:32]
    width_bitstring = bits[32:64]
    height = int(height_bitstring, 2)
    width = int(width_bitstring, 2)
    print('Height: {}, width: {}'.format(height, width))
    # Get image vals from bits after header
    img = bits_to_img(bits[64:], height, width)
    img.show()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = 'hide_image.png'
    decode_img(target)
