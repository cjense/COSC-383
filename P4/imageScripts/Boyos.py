"""Red herring?"""

from sys import path
path.append('C:/Users/clair/Desktop/Coding/COSC-383/P4/')

import imageio.v3 as iio
import tempfile as tmp

import utils
import decode_image as di
import decode_text as dt
import decode_image2 as di2

filename = '../PNGs/Boyos.png'
img = iio.imread(filename)

# bits = utils.get_bits2(img, axis=0, func=lambda px: [str(x&1) for x in px])
# # Parse header
# height_bitstring = bits[0:32]
# width_bitstring = bits[32:64]
# height = int(height_bitstring, 2)
# width = int(width_bitstring, 2)
# print('Height: {}, width: {}'.format(height, width))

# saved decoded images already
# for i in range(0, 3):
#     bits = utils.getBitsFromSingleChannel(img, i)
#     print("From channel ", i)
#     # print(dt.bits_to_str(bits, 1000))
#     decoded = di2.bits_to_img(bits, height, width)
#     utils.save(decoded, '../decodedimages/Boyos'+str(i)+'.png')

    # img = utils.magnify_LSB(magnified)
    # img.show()

filename = '../decodedimages/Boyos0.png'
img = iio.imread(filename)

string = dt.decode_txt_new(filename, 1000)
print(string)

# magnified = utils.magnify_LSB(img)
# utils.save(magnified, '../decodedimages/Boyos0_magnified.png')

# decoded = tmp.NamedTemporaryFile()
# dec_img = di.bits_to_img(bits[64:], height, width)
# dec_img.show()
# utils.save(dec_img, '../decodedimages/'+decoded.name+'.png')

# magnified = tmp.NamedTemporaryFile()
# mag_img = utils.magnify_LSB(iio.imread('../decodedimages/'+decoded.name+'.png'))
# utils.save(mag_img, '../decodedimages/'+magnified.name+'_decoded.png')
# mag_img.show()

# #print(dt.default_decode_txt(decoded.name+'.png'))

# bits2 = utils.get_bits2(iio.imread(decoded.name+'.png'), func=only_red, axis=1)
# num_chars = int(bits2[:32], 2)
# print(num_chars)
# print(dt.bits_to_str(bits2[32:], num_chars))