import imageio as iio
import numpy as np
from PIL import Image as im

def get_bits(img, bitmask=1):
    """Given an iio image object and a bitmask to select bits from each pixel channel, return a bitstring of the selected bits"""
    height, width, _ = img.shape
    bits = ""
    for r in range(height):
        for c in range(width):
            for x in range(3):
                bits += str(img[r, c, x] & bitmask)
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


def magnify_lsb(img):
    """Magnify the least significant bit in each pixel channel to be either 0 or 255"""
    # Initialize an array the size of the original image
    height, width, _ = img.shape
    array = np.zeros((height, width, 3), np.uint8)
    # For each row, column, channel, magnify the least significant bit
    for r in range(height):
        for c in range(width):
            for x in range(3):
                array[r, c, x] = 0 if (img[r, c, x] << 7) & 255 == 0 else 255
    # Read the array as a PIL Image and return it
    img = im.fromarray(array, mode='RGB')
    return img
