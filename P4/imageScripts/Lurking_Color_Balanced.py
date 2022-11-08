from sys import path
path.append('C:/Users/clair/Desktop/Coding/COSC-383/P4/')
import utils
import imageio.v3 as iio
import decode_text as dt

filename = '../decodedImages/Lurking_Color_Balanced_decoded_magnified.png'
img = iio.imread(filename)

for i in range(0, 3):
    bits = utils.getBitsFromSingleChannel(img, i)
    print("Bits for channel ", i)
    print(dt.bits_to_str(bits, 340))