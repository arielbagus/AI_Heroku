import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imshow, imread
from skimage.color import rgb2yuv, rgb2hsv, rgb2gray, yuv2rgb, hsv2rgb
from scipy.signal import convolve2d

dog = imread('fire_dog.png')
plt.figure(num=None, figsize=(8, 6), dpi=80)
imshow(dog);

def multi_convolver(image, kernel, iterations):
    for i in range(iterations):
        image = convolve2d(image, kernel, 'same', boundary = 'fill',
                           fillvalue = 0)
    return image
multi_convolver(dog, gaussian, 2)

dog_grey = rgb2gray(dog)
convolved_image = multi_convolver(dog_grey, gaussian, 2)
plt.figure(num=None, figsize=(8, 6), dpi=80)
imshow(convolved_image);