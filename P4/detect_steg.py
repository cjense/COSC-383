import sys

import imageio as iio
import matplotlib.pyplot as plt

import utils

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = 'hide_image.png'
    img = iio.imread(target)
    utils.magnify_LSB(img).show()
    utils.get_LSB_histogram(img)
    plt.show()
