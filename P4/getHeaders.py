import utils
import os
import imageio.v3 as iio

def getheader(filename, size, endianness):
    img = iio.imread(filename)
    # Extract least-significant bits as string
    bits = utils.get_bits(img, lambda x: x&1)

    size_2 = size // 2

    height_bitstring = bits[0:size_2]
    width_bitstring = bits[size_2:size]
    height = int(height_bitstring, 2)
    width = int(width_bitstring, 2)
    print("Header size is ", size)
    if endianness == 'big':
        print('Big Endian Height: {}, width: {}'.format(int(utils.big_endian(height_bitstring)), int(utils.big_endian(width_bitstring))))
    elif endianness == 'little':
        print('Little Endian Height: {}, width: {}'.format(height, width))


for filename in os.listdir('PNGs'):
    filepath = 'PNGs/' + filename
    img = iio.imread(filepath)
    print("***********************************************************************")
    print("Image is ", filename)

    getheader(filepath, 16, 'big')
    getheader(filepath, 32, 'big')
    getheader(filepath, 64, 'big')

    getheader(filepath, 16, 'little')
    getheader(filepath, 32, 'little')
    getheader(filepath, 64, 'little')


