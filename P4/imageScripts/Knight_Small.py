from sys import path
path.append('C:/Users/clair/Desktop/Coding/COSC-383/P4/')
import utils
import imageio.v3 as iio
import decode_image as di
import numpy as np
from PIL import Image as im
import decode_text as dt
import hiddenimage as hi

filename = '../PNGs/Knight_Small.png'
img = iio.imread(filename)

hi.get_hw(filename)

di.decode_img(filename,'nosavename')