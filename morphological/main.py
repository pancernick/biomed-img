import os
import matplotlib.pyplot as plt
from skimage.data import data_dir
from skimage.util import img_as_ubyte
from skimage import io

from skimage.morphology import erosion, dilation, opening, closing
from skimage.morphology import black_tophat, skeletonize, convex_hull_image
from skimage.morphology import disk


def plot_comparison(original, filtered, filter_name):

    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(8, 4), sharex=True,
                                   sharey=True)
    ax1.imshow(original, cmap=plt.cm.gray)
    ax1.set_title('original')
    ax1.axis('off')
    ax2.imshow(filtered, cmap=plt.cm.gray)
    ax2.set_title(filter_name)
    ax2.axis('off')
    # plt.show()


def main():

    # ***PHANTOM*** #
    orig_phantom = img_as_ubyte(
                io.imread(os.path.join(data_dir, "phantom.png"), as_gray=True))
    # erosion
    selem = disk(10)
    eroded = erosion(orig_phantom, selem)
    plot_comparison(orig_phantom, eroded, 'erosion')
    # dilation
    dilated = dilation(orig_phantom, selem)
    plot_comparison(orig_phantom, dilated, 'dilation')

    # opening
    opened = opening(orig_phantom, selem)
    plot_comparison(orig_phantom, opened, 'opening')

    # closing
    phantom = orig_phantom.copy()
    phantom[10:30, 200:210] = 0  # stworzenie nieciągłości zewn. okręgu

    closed = closing(phantom, selem)
    plot_comparison(phantom, closed, 'closing')

    # ***SKELETON*** #
    horse = io.imread(os.path.join(data_dir, "horse.png"), as_gray=True)

    # skeletonize
    sk = skeletonize(horse == 0)
    plot_comparison(horse, sk, 'skeletonize')

    plt.show()


main()
