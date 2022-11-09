from sys import path
path.append('C:/Users/clair/Desktop/Coding/COSC-383/P4/')
import utils
import imageio.v3 as iio
import decode_image as di
import numpy as np
from PIL import Image as im
import decode_text as dt
import hiddenimage as hi
import itertools as it

filename = '../PNGs/AmVase.png'
img = iio.imread(filename)

# I think the header is 56 bits long
# Use itertools for this

# Use itertools to find cartesian product of RGB channels
rgb = []
for i in range[0, 1, 2]:
    rgb[i] = utils.getBitsFromSingleChannel(img, i)
    it.product(range(0, 3), repeat=3)


# bytes = utils.bits_to_bytes(bits)
# i=0  # Counter for which byte we're working with
# # Iterate across channels, columns, rows to insert bytes appropriately
# for h in range(height):
#     for w in range(width):
#         for x in range(3):
#             array[h, w, x] = int(bytes[i], 2)
#             i += 1
# # Create image from array
# img = im.fromarray(array, mode='RGB')
# img.show()

# Extract bits from each channel (RGB and alpha)
# for i in range(0, 3):
#     bits = utils.getBitsFromSingleChannel(img, i)
#     print("Bits for channel ", i)
#     print(dt.bits_to_str(bits, 400))

# Extract height and width
# hi.get_hw(filename)
# height = 59, width is unclear

# di.decode_img(filename, 'nosavename')

# bits = utils.get_bits(img, 59, None, lambda x: x&1)  # lambda gets LSB of x
# bytes = utils.bits_to_bytes(bits)
# img = di.bits_to_img(bits[64:], 59, 59)
# img.show()

# # Parse header
# height_bitstring = bits[0:32]
# width_bitstring = bits[32:64]
# height = int(height_bitstring, 2)
# width = int(width_bitstring, 2)
# print('Height: {}, width: {}'.format(utils.big_endian(height_bitstring), utils.big_endian(width_bitstring)))
# # Get image vals from bits after header
# img = di.bits_to_img(bits[64:], height, width)
# img.show()
# utils.save(img, savename)