from sys import path
path.append('C:/Users/clair/Desktop/Coding/COSC-383/P4/')
import utils
import imageio.v3 as iio
import decode_text as dt
import decode_image2 as dt2

# Load in initial encoded image
filename = '../PNGs/Lurking_Color_Balanced.png'
img = iio.imread(filename)

# Decode image
img = dt2.default_decode_img(filename)
img.show()

# Load in decoded image
filename2 = '../decodedimages/Lurking_Color_Balanced_decoded1.png'
img2 = iio.imread(filename2)

# Extract text from Red channel of decoded image
bits = utils.getBitsFromSingleChannel(img2, 2)
print("Text from Blue channel:")
print("")
print(dt.bits_to_str(bits[32:], 100))