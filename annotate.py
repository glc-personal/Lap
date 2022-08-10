#!/usr/bin/env python3

import sys
import napari
import argparse as ap
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def check_file_exists(fpath):
	import os

	return os.path.isfile(fpath)

#def check_if_pixel_in_rgb_window(pixel_nparray, rgb, delta):
	

def change_all_pixels_with_exception(nparray_image, delta=(15,15,15), rgb_exception=(254,254,254), rgb_rest=(0,0,0)):
	# Make all pixels that are not the same color as exception the rgb_rest color.
	nparray_image[np.all(nparray_image != rgb_exception, axis=-1)] = rgb_rest
	#for pixel in nparray_image:

if __name__ == '__main__':
	# Argument Parser
	parser = ap.ArgumentParser(description="Open napari for annotating the specified image path")
	parser.add_argument('-i', '--image', help="path to image for annotation", required=True)
	args = vars(parser.parse_args())

	# Get the image path
	img_path = args['image']

	# Check if the file exists, preprocess the image to get just the roads, then open napari for annotating the curves.
	if check_file_exists(img_path):
		# Convert the png to a numpy array
		image = cv.imread(img_path)

		# Get just the roads.
		change_all_pixels_with_exception(image)

		# Open the napari viewer
		viewer = napari.view_image(image, rgb=True)
		napari.run()
	else:
		sys.exit("Error: {0} does not exist ... exiting".format(img_path))
