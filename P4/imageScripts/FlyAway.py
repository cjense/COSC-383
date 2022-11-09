from sys import path
path.append('C:/Users/clair/Desktop/Coding/COSC-383/P4/')
import utils
import imageio.v3 as iio
import decode_image as di
import numpy as np
from PIL import Image as im
import decode_text as dt
import hiddenimage as hi

filename = '../PNGs/FlyAway.png'
img = iio.imread(filename)

# Something is in the red channel
# Why say in four lines what you could say in one?

dt.decode_txt_new(filename)

# Grabbed second LSB from channels, tried BGR and RGB, tried axis=0 and axis=1 for each

# height_bitstring = bits[0:32]
# width_bitstring = bits[32:64]
# height = int(height_bitstring, 2)
# width = int(width_bitstring, 2)
# print('Height: {}, width: {}'.format((height), (width)))

# bits = utils.getBitsFromSingleChannel(img, 0)
# height = bits[0:32]
# width = bits[32:64]

# # string = dt.bits_to_str(bits, 1000)
# # print(string)

# img = (hi.bits_to_img(bits, height, width))
# img.show()

# hi.get_hw(filename)

# di.decode_img(filename,'nosavename')