import sys

import imageio as iio
import matplotlib.pyplot as plt

import utils

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = 'sampleImages/hide_image.png'
    img = iio.imread(target)
    utils.magnify_LSB(img).show()
    utils.get_LSB_histogram(img)
    plt.show()

def grab_hist(target, savename):
    img = iio.imread(target)
    hist = utils.get_LSB_histogram(img)

    utils.save(hist, savename)

def grab_magnified(target, savename):
    img = iio.imread(target)
    magnified = utils.magnify_LSB(img)

    utils.save(magnified, savename)
