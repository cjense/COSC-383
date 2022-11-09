import imageio.v3 as iio
import numpy as np
from PIL import Image as im
import sys
import utils
import os

#img = iio.imread("hide_text.png")

# function to extract bits - same as text extraction
def get_bits(img, bitmask):
    # Given an image and a bitmask to select bits from each pixel channel, return a list of the selected bits
    height, width, _ = img.shape
    bits = []
    for r in range(height):
        for c in range(width):
            for x in range(3):
                bits.append(str(img[r, c, x] & bitmask))
    return bits

# function to extract 64-bit header, height, and width
def get_hw(filename):
    img = iio.imread(filename)
    # Extract least-significant bits as string
    bits = utils.get_bits2(img, lambda x: x&1)  # lambda gets LSB of x
    # Parse header
    height_bitstring = bits[0:32]
    width_bitstring = bits[32:64]
    height = int(height_bitstring, 2)
    width = int(width_bitstring, 2)
    print('Height: {}, width: {}'.format(height, width))

def bits_to_bytes(bits):
    # Given a list of bits, break them into bitstrings of length 8
    bytes = []
    for i in range(len(bits) // 8):
        byte = ''.join(bits[i*8:(i+1)*8])
        bytes.append(byte)
    return bytes

# function to convert a list of bits into an image
def bits_to_img(bits, height, width):
    # Create an array of zeroes in the desired final shape
    array = np.zeros((height, width, 3), np.uint8)
    # Convert bits to bytes
    bytes = bits_to_bytes(bits)
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

# big to little endian convertor
def big_endian(bits):
    # Chunk bits into bytes
    bytes = bits_to_bytes(bits)
    # Reverse order of bytes
    bytes.reverse()
    # Parse binary as int and return
    return int(''.join(bytes), 2)

#print(big_endian(['0', '0', '0', '0', '0', '0', '0', '0',
#                   '1', '1', '1', '1', '1', '1', '1', '1']))

def decode_img(filename, savename):
    # Load image
    img = iio.imread(filename)
    # Extract least-significant bits
    bits = utils.get_bits2(img, 1)
    # Parse header
    height_bitstring = ''.join(bits[0:32])
    width_bitstring = ''.join(bits[32:64])
    height = int(height_bitstring, 2)
    width = int(width_bitstring, 2)
    print('Height: {}, width: {}'.format(height, width))
    # Get image vals from bits after header
    img = bits_to_img(bits[64:], height, width)
    img.show()
    img.save(savename)