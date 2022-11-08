import utils
import os
import imageio.v3 as iio

def getheader(filename, size, endianness):
    img = iio.imread(filename)
    # Extract least-significant bits as string
    bits = utils.get_bits(img, lambda x: x&1)

    height_bitstring = bits[0:(size/2)]
    width_bitstring = bits[(size/2):size]
    height = int(height_bitstring, 2)
    width = int(width_bitstring, 2)
    print("Header size is ", size)
    if endianness == 'big':
        print('Height: {}, width: {}'.format(utils.big_endian(height_bitstring), utils.big_endian(width_bitstring)))
    elif endianness == 'little':
        print('Height: {}, width: {}'.format(height, width))


for filename in os.listdir('PNGs'):
    filepath = 'PNGs/' + filename
    img = iio.imread(filepath)

    getheader(filepath, 16, 'big')
    getheader(filepath, 32, 'big')
    getheader(filepath, 64, 'big')

    getheader(filepath, 16, 'little')
    getheader(filepath, 32, 'little')
    getheader(filepath, 64, 'little')


