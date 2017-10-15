#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np
import requests
import os.path

class BoundingBox(object):
    def __init__(self, image):
        self.image = image

        if hasattr(image, 'read'):  # When image is a file-like object.
            self.im = np.array(Image.open(image), dtype=np.uint8)
        elif os.path.isfile(image):  # When image is a file path.
            self.im = np.array(Image.open(image), dtype=np.uint8)
        else:  # Default treat it as a URL (string).
            response = requests.get(self.image, stream=True).raw
            self.im = np.array(Image.open(response), dtype=np.uint8)


    def define_box(self, x, y, height, width):
        self.x = x
        self.y = y
        self.h = height
        self.w = width

    def display(self, name):

        # Create figure and axes
        fig,ax = plt.subplots(1)

        # Display the image
        ax.imshow(self.im)

        # Create a Rectangle patch
        rect = patches.Rectangle((self.x,self.y),self.h,self.w,linewidth=1,edgecolor='r',facecolor='none')

        # Add text
        font = {'family': 'serif',\
                'color':  'blue',\
                'weight': 'normal',\
                'size': 40,\
               }
        plt.text(self.x + self.h, self.y + self.w, name, fontdict=font)

        # Add the patch to the Axes
        ax.add_patch(rect)

        plt.show()

if __name__ == '__main__':
    img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
    bbox = BoundingBox(img_url)
    bbox.define_box(50, 100, 40, 30)
    bbox.display('Biel')
