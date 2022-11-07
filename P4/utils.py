import imageio as iio
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image as im
import itertools as it

def get_bits_iter(img):
    height, width, _ = img.shape
    for h in range(height):
        for w in range(width):
            for c in range(3):
                it.product(img[h, w, c])
    # bits = it.product(range(height), range(width), range(3))
    # bits = 

    return bits

def getBitsFromSingleChannel(img, channel):
    """Given an image and a channel, return a bitstring.

    @param img: imageio image object
    @param channel: channel to extract bits from
    @return: string of extracted bits in the image, in left-to-right,
        top-to-bottom order
    """
    height, width, _ = img.shape
    string = []
    for r in range(height):
        for c in range(width):
            string.append(img[r, c, channel]&1)

    return string

def get_bits(img, func=lambda x: x&1):
    """Given an image and a function to select bits from each pixel channel,
    return a bitstring of the selected bits.

    @param img: imageio image object
    @param func: function that takes a channel value and returns zero or more
        bits (default returns LSB)
    @return: string of extracted bits in the image, in left-to-right,
        top-to-bottom, RGB order
    """
    height, width, _ = img.shape
    bits = ""
    for r in range(height):
        for c in range(width):
            for x in range(3):
                bits += str(func(img[r, c, x]))
    return bits


def bits_to_bytes(bitstring):
    """Given a bitstring, break them into a list of bitstrings of length 8"""
    bytes = []
    for i in range(len(bitstring) // 8):
        byte = ''.join(bitstring[i*8:(i+1)*8])  # Drops any at the end that don't fit into a multiple of 8
        bytes.append(byte)
    return bytes


def big_endian(bitstring):
    """Given a bitstring, read as a big-endian int"""
    bytes = []
    for i in range(len(bitstring), 0, -8):
        bytes.append(bitstring[i-8:i])  # Drops leading bits that don't fit into a multiple of 8
    print(bytes)
    converted = ''.join(bytes)
    print(converted)
    return int(converted, 2)


def magnify_LSB(img):
    """Magnify the least significant bit in each pixel channel to be either 0 or
    255
    
    @param img: an imageio image
    @return: a PIL image whose pixel-channel values are the amplified values of
        the corresponding pixel-channels in the original"""
    # Initialize an array the size of the original image
    height, width, _ = img.shape
    array = np.zeros((height, width, 3), np.uint8)
    # For each row, column, channel, magnify the least significant bit
    for r in range(height):
        for c in range(width):
            for x in range(3):
                array[r, c, x] = 0 if (img[r, c, x] << 7) & 255 == 0 else 255
    # Read the array as a PIL Image and return it
    magnified = im.fromarray(array, mode='RGB')
    return magnified


def get_LSB_histogram(img):
    """Show a histogram of the permutations of LSBs in a 2x2 square for each
    pixel across an image"""
    fig, ax = plt.subplots(1, 1)  # Get container for returning plot
    # 2 values for each LSB ^ 3 channels per pixel ^ 4 pixels per grid = 4096 permutations
    # Read string of LSBs as binary number 0 <= x < 4096
    vals = []
    height, width, _ = img.shape
    # For each row, column in the image (excluding bottom and right edges due to bounds)
    for r in range(height-1):
        for c in range(width-1):
            # Read the LSBs in the 2x2 grid
            val = ''
            for dy in [0, 1]:
                for dx in [0, 1]:
                    for x in range(3):
                        val += str(img[r+dy, c+dx, x] & 1)
            vals.append(int(val, 2))
    ax.hist(vals, bins=4096)
    return fig


def save(img, filename):
    """Utility to abstract saving any of the various types of images/graphics
    used in this codebase"""
    # Import types here to keep top of file cleaner
    from imageio.core.util import Array as iio_img
    from matplotlib.figure import Figure as plt_fig
    from PIL.Image import Image as PIL_img

    if type(img) == iio_img:
        iio.imwrite(filename, img)
    elif type(img) == plt_fig:
        img.savefig(filename)
    elif type(img) == PIL_img:
        img.save(filename)
    else:
        raise TypeError("Unrecognized image type")
