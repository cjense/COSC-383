from sys import path
path.append('C:/Users/clair/Desktop/Coding/COSC-383/P4/')
import utils
import imageio.v3 as iio
import decode_text as dt

# Load in initial encoded image
filename = '../PNGs/OhHai.png'
img = iio.imread(filename)

# Extract text from Red channel of image
bits = utils.getBitsFromSingleChannel(img, 2)
print("Text from Red channel:")
print("")
print(dt.bits_to_str(bits[32:], 500))