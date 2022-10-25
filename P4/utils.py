def get_bits(img, bitmask=1):
    """Given an iio image object and a bitmask to select bits from each pixel channel, return a bitstring of the selected bits"""
    height, width, _ = img.shape
    bits = ""
    for r in range(height):
        for c in range(width):
            for x in range(3):
                bits += str(img[r, c, x] & bitmask)
    return bits


def bits_to_bytes(bitstring):
    """Given a bitstring, break them into a list of bitstrings of length 8"""
    bytes = []
    for i in range(len(bitstring) // 8):
        byte = ''.join(bitstring[i*8:(i+1)*8])  # Drops any at the end that don't fit into a multiple of 8
        bytes.append(byte)
    return bytes


def big_endian(bitstring):
    """Given a bitstring, read as a big-endian int"""
    bytes = []
    for i in range(len(bitstring), 0, -8):
        bytes.append(bitstring[i-8:i])  # Drops leading bits that don't fit into a multiple of 8
    print(bytes)
    converted = ''.join(bytes)
    print(converted)
    return int(converted, 2)