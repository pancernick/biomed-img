# biomed-img
A short project on  the morphological filtering and the image convolution

## IMAGE CONVOLUTION
### Short description
A small script that takes given image (also a colour image) and perform
a convolution with given parameters:
- a kernel matrix
- a padding
- a stride

### Usage
Written in `python v3.6`.
To run the script you need to install a few required libraries and enter parameters
in specific way.
#### Install:
You need to install:
- [numpy](https://www.scipy.org/install.html)
- [matplotlib](https://matplotlib.org/users/installing.html)
- [pillow](https://pillow.readthedocs.io/en/5.3.x/installation.html)

When using the `conda` environment, just go with `conda install <package-name>`

#### Command line parameters entering:
Flags for parameters (type):
- image path: `--image` (str)
- padding: `--padding` (int)
- stride: `--stride` (int)
- kernnel matrix: `--matrix` (str) in format " <first row>; <second row>; <third row>"
For example:
`python conv_wo_lib.py --image "conv_img2.jpg" --padding 3 --stride 1 --kernel "0 1 0; 1 1 1; 0 1 0"`
