import sys

import imageio.v3 as iio

import utils

def bits_to_str(bits, num_chars):
    """Given a list of bits, read them as a string
    
    @param bits: a bitstring expected to have at least 8*num_chars bits,
        representing the ASCII values of the characters of the text
    @param num_chars: how many characters of text to read
    @return: the bits read as num_chars worth of text"""
    # Chunk bits into bytes/chars
    bytes = utils.bits_to_bytes(bits[:num_chars*8])
    # Convert bytes into ints for ASCII chars
    ascii = [int(b, 2) for b in bytes]
    # Convert chars to string
    string = ''.join(chr(c) for c in ascii)
    return string


def decode_txt(filename):
    """Read encoded text from a given image file"""
    # Read in the image
    img = iio.imread(filename)
    # Extract bitstring
    bits = utils.get_bits(img, lambda x: x&1)  # lambda gets LSB of x
    # Read first 32 bits as header and parse as number of characters
    chars_bitstring = bits[0:32]
    num_chars = int(chars_bitstring, 2)
    # Get number of chars from bitstring after header
    string = bits_to_str(bits[32:], num_chars)
    print(string)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = 'hide_text.png'
    decode_txt(target)