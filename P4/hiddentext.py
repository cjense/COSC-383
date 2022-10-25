# function for extracting the 32-bit header

# function for extracting the bytes

# function for translating bytes to chars
# with parameter denoting how many of the LSBs to extract

import imageio.v3 as iio

# function to extract bits - same as text extraction
def get_bits(img, bitmask):
    # Given an image and a bitmask to select bits from each pixel channel, return a list of the selected bits
    height, width, _ = img.shape
    bits = []
    for r in range(height):
        for c in range(width):
            for x in range(3):
                bits.append(str(img[r, c, x] & bitmask))
    return bits


def bits_to_bytes(bits):
    # Given a list of bits, break them into bitstrings of length 8
    bytes = []
    for i in range(len(bits) // 8):
        byte = ''.join(bits[i*8:(i+1)*8])
        bytes.append(byte)
    return bytes


# function to convert a list of bits into text
def bits_to_str(bits, num_chars):
    # Chunk bits into bytes/chars
    bytes = bits_to_bytes(bits[:num_chars*8])
    # Convert bytes into ints for ASCII chars
    codes = [int(b, 2) for b in bytes]
    # Convert chars to string
    string = ''.join(chr(c) for c in codes)
    return string



# big to little endian convertor
def big_endian(bitstring):
    bytes = []
    for i in range(len(bitstring), 0, -8):
        bytes.append(bitstring[i-8:i])
    print(bytes)
    converted = ''.join(bytes)
    print(converted)
    return int(converted, 2)

#print(big_endian('0000000011111111'))
    

def decode_txt(filename):
    # Read in the image
    img = iio.imread(filename)
    # Extract bitstring
    bits = get_bits(img, 1)
    # Read first 32 bits as header and parse as number of characters
    chars_bitstring = ''.join(bits[0:32])
    num_chars = int(chars_bitstring, 2)
    # Get number of chars from bitstring after header
    string = bits_to_str(bits[32:], num_chars)
    print(string)

decode_txt('hide_text.png')