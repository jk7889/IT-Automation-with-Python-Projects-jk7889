#!/usr/bin/env python3

from PIL import Image
import os


def fixer(image):
    """To change resolution and format of all images in supplier-data/images/ folder"""
    try:
        # Removing opacity layer from image by converting it to RGB from RGBA
        im = Image.open("supplier-data/images/" + image).convert("RGB")
        x = image.split(".")

        # Changing resolution to 600x400 pixel and image format to .jpeg
        im.resize((600, 400)).save("supplier-data/images/" + x[0] + ".jpeg")
    except:
        # Try Except block will ignore all those files which are not images
        pass


if __name__ == "__main__":
    """List all files and directories in supplier-data/images/ directory and converting it to the new specifications"""
    images = os.listdir("supplier-data/images/")
    for pic in images:
        fixer(pic)


