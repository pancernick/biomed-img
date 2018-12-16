import numpy as np
import argparse
import matplotlib.pyplot as plt


def my_conv2d(g_kernel, image, stride, padding):
        g_kernel = np.flipud(np.fliplr(g_kernel))
        output_img_wshape = int((image.shape[0]-g_kernel.shape[0]+2*padding)/stride + 1)
        output_img_hshape = int((image.shape[1]-g_kernel.shape[1]+2*padding)/stride + 1)
        output = np.zeros([output_img_wshape, output_img_hshape, image.shape[2]])
        # Add zero padding to the input image
        image_padded = np.zeros((
                image.shape[0] + padding*2,
                image.shape[1] + padding*2,
                image.shape[2]))
        # import pdb; pdb.set_trace()
        image_padded[padding:-padding, padding:-padding, :] = image  # fencing
        for ch in range(0, image.shape[2]):
            print(f"In progress: convolution of channel no {ch+1}")
            for y in range(image.shape[1]):
                if stride*y <= image.shape[1]:
                    for x in range(image.shape[0]):
                        if stride*x <= image.shape[0]:
                            output[x, y, ch] = (
                                g_kernel*image_padded[(stride*x):(stride*x+g_kernel.shape[0]),
                                                      (stride*y):(stride*y+g_kernel.shape[1]),
                                                      ch]).sum()
                        continue
                continue
        return output


def str2bool(v):
    if v.lower() in ("yes", "true", "t", "y", "1"):
        return True
    elif v.lower() in ("no", "false", "f", "n", "0"):
        return False
    else:
        raise argparse.ArgumentTypeError("Boolean value expected.")


def cmd_arguments(parser):
    """"
    Add model specific args to the parse
    Args:
        - parser : argparse.ArgumentParser() object
    """ ""
    group = parser.add_argument_group(
        title="Cmd Arguments",
        description="""
          These include an image filename, a padding, a stride
          and a desired  convolution kernel.
          They will be passed in as normal command line flags.
        """,
    )

    group.add_argument("--image", type=str, required=True)
    group.add_argument("--padding", type=int, required=True)
    group.add_argument("--stride", type=int, required=True)
    group.add_argument("--kernel", type=str, required=True)

    return group


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    cmd_arguments(parser)
    args = parser.parse_args()

    # read image
    im = plt.imread(args.image).astype(float)
    im = im/255   # normalise to 0-1, it's easier to work in float space
    print(f"Shape of the original image: {im.shape}")

    # set kernel type
    g_kernel = np.squeeze(np.asarray(np.matrix(args.kernel)))

    # conv it!
    output_img = my_conv2d(g_kernel, im, args.stride, args.padding)

    # show plots
    print(f"Shape of the conv image: {im.shape}")

    plt.subplot(1, 2, 1)
    plt.imshow(im)
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(output_img)
    plt.title('Conv image')

    plt.show()
