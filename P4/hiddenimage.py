import imageio

img = imageio.imread("hide_text.png")

# function to extract bits - same as text extraction
def get_bits(img, bitmask):
    height, width, _ = img.shape
    bits = []
    for r in range(height):
        for c in range(width):
            for x in range(3):
                bits.append(img[r, c, x] & bitmask)
    print(bits)
    return bits

img = imageio.imread("hide_text.png")
get_bits(img, 1)

# function to extract 64-bit header, height, and width
def get_hw(img):
    height, width, _ = img.shape
    print("Height:", height, "Width:", width)
    return [height, width]

# function to convert a string of bytes into an image
def bytes_to_img(bytes):
    return img

def img_to_bytes(img):
    png_encoded = imageio.imwrite("<bytes>", img, extension=".png")
    return png_encoded

# big to little endian convertor
def big_endian(bits):
    bytes = []
    for i in range( (len(bits) // 8) + 1 ):
        bytes.append(bits[(-8*i)-1 : (-8*i)])
    

def read_img(filename):
    img = imageio.imread(filename)
    bits = get_bits(img, 1)
    width = big_endian(bits[0:32])
    height = big_endian(bits[32:64])
