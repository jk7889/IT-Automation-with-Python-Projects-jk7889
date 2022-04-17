#!/usr/bin/env python3
import requests
import os


def main():
	"""Uploads all jpeg images in the supplier-data/images/ directory to the URL given below"""
	url = "http://localhost/upload/"

	# Listing files and directories in supplier-data/images/ directory
	images = os.listdir("supplier-data/images")

	# Upload the images with jpeg extension
	for img in images:
		if img.endswith(".jpeg"):
			with open("supplier-data/images/" + img, "rb") as opened:
				r = requests.post(url, files={'file': opened})


if __name__ == "__main__":
	# Calling main function
	main()
