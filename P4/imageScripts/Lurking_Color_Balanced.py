from sys import path
path.append('C:/Users/clair/Desktop/Coding/COSC-383/P4/')
import utils
import imageio.v3 as iio
import decode_text as dt
import decode_image2 as dt2

# filename = '../PNGs/Lurking_Color_Balanced.png'
# # img = iio.imread(filename)

# img = dt2.default_decode_img(filename)
# utils.save(img, '../decodedimages/Lurking_Color_Balanced_decoded1.png')

filename2 = '../decodedimages/Lurking_Color_Balanced_decoded1.png'
img2 = iio.imread(filename2)

for i in range(0, 3):
    bits = utils.getBitsFromSingleChannel(img2, i)
    print("Text from channel ", i)
    print("")
    print(dt.bits_to_str(bits, 1000))
try:
    bits = utils.getBitsFromSingleChannel(img2, 4)
except:
    print("No alpha channel")

# img2 = utils.magnify_LSB(img2)
# img2.show()


# dt.decode_txt(filename2, 1000)

# for i in range(0, 3):
#     bits = utils.getBitsFromSingleChannel(img, i)
#     print("Bits for channel ", i)
#     print(dt.bits_to_str(bits, 340))