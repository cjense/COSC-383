from sys import path
path.append('C:/Users/clair/Desktop/Coding/COSC-383/P4/')
import utils
import imageio.v3 as iio
import decode_image as di
import numpy as np
from PIL import Image as im
import decode_text as dt
import hiddenimage as hi
import decode_image2 as di2

filename = '../PNGs/Waaaarm.png'
img = iio.imread(filename)

img = di2.default_decode_img(filename)
img.show()


bits = utils.getBitsFromSingleChannel(img, 0)
string = dt.bits_to_str(bits, 2048)
print(string)

print('***************************')

string1 = dt.bits_to_str(bits[1:], 8647)
print(string1)


# 8648 total chars, beginning char is !

img = di.bits_to_img(bits[1:], 100, 100)
img.show()