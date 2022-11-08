import utils
import os
import imageio.v3 as iio
import decode_text as dt

for filename in os.listdir('PNGs'):
    filepath = 'PNGs/' + filename
    img = iio.imread(filepath)
    print("***********************************************************************")
    print("Image is ", filename)
    # for i in range(0, 3):
    bits = utils.getBitsFromSingleChannel(img, 4)
    print("Text from channel ", 4)
    print("")
    print(dt.bits_to_str(bits, 10000))
    print("")
    try:
        bits = utils.getBitsFromSingleChannel(img, 4)
    except:
        print("No alpha channel")