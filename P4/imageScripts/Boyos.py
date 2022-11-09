from sys import path
path.append('C:/Users/clair/Desktop/Coding/COSC-383/P4/')

import imageio.v3 as iio
import utils
import decode_text as dt
import decode_image2 as di2

filename = '../PNGs/Boyos.png'
img = iio.imread(filename)

for i in range(0, 3):
    # Extract images - one for each channel
    bits = utils.getBitsFromSingleChannel(img, i)
    print("From channel ", i)
    decoded = di2.bits_to_img(bits[64:], 240, 320)
    decoded.show()

    # Magnify the newly decoded images
    # magnified = utils.magnify_LSB(decoded)
    # magnified.show()

#############################################################################
# Boyos0
# THIS IMAGE HAS A HEADER GOING FROM TOP TO BOTTOM

print("")
print("Image is Boyos0 (Red channel of Boyos.png)")

def decode_txt_boyos0(filename):
    """Read encoded text from a given image file"""
    # Read in the image
    img = iio.imread(filename)
    # Extract bitstring
    bits = utils.get_bits_ttb(img)
    # Read first 32 bits as header and parse as number of characters
    chars_bitstring = bits[0:32]
    num_chars = int(chars_bitstring, 2)
    # Get number of chars from bitstring after header
    string = dt.bits_to_str(bits[32:], num_chars)
    print(string)

boyos0 = '../decodedimages/Boyos0.png'
img_boyos0 = iio.imread(boyos0)

decode_txt_boyos0(boyos0)

#############################################################################
# Boyos1

print("")
print("Image is Boyos1 (Green channel of Boyos.png)")

def decode_txt_boyos1(filename):
    """Read encoded text from a given image file"""
    # Read in the image
    img = iio.imread(filename)
    # Extract bitstring
    bits = utils.get_bits(img)
    # Read first 32 bits as header and parse as number of characters
    chars_bitstring = bits[0:32]
    num_chars = int(chars_bitstring, 2)
    # Get number of chars from bitstring after header
    string = dt.bits_to_str(bits[32:], num_chars)
    print(string)

boyos1 = '../decodedimages/Boyos1.png'
img_boyos1 = iio.imread(boyos1)

bits = utils.getBitsFromSingleChannel(img_boyos1, 0)
print("From Red channel:")
str = dt.bits_to_str(bits[32:], 100)
print(str)

#############################################################################
# Boyos2

print("")
print("Image is Boyos2 (Blue channel of Boyos.png)")

def decode_txt_boyos2(filename, num_chars):
    """Read encoded text from a given image file"""
    # Read in the image
    img = iio.imread(filename)
    # Extract bitstring
    bits = utils.get_bits(img)
    string = dt.bits_to_str(bits[32:], num_chars)
    print(string)

boyos2 = '../decodedimages/Boyos2.png'
img_boyos2 = iio.imread(boyos2)

bits = utils.getBitsFromSingleChannel(img_boyos2, 1)
print("From Blue channel:")
print(dt.bits_to_str(bits[32:], 100))