from NeuralNetwork.NeuralNetwork import NeuralNetwork
import numpy as np


'''
    This Example opens an Image and transform the image using Pointilize.
    We also use a sepia filter as an optional step.
    You need PILLOW (Python Imaging Library fork) and Python 3.5
    -Isai B. Cicourel
'''

# Imported PIL Library
from PIL import Image, ImageDraw


# Open an Image
def open_image(path):
    newImage = Image.open(path)
    return newImage


# Save Image
def save_image(image, path):
    image.save(path, 'png')


# Create a new image with the given size
def create_image(i, j):
    image = Image.new("RGB", (i, j), "white")
    return image


# Get the pixel from the given image
def get_pixel(image, i, j):
    # Inside image bounds?
    width, height = image.size
    if i > width or j > height:
        return None

    # Get Pixel
    pixel = image.getpixel((i, j))
    return pixel


# Limit maximum value to 255
def get_max(value):
    if value > 255:
        return 255

    return int(value)


# Sepia is a filter based on exagerating red, yellow and brown tones
# This implementation exagerates mainly yellow with a little brown
def get_sepia_pixel(red, green, blue, alpha):
    # Filter type
    value = 0

    # This is a really popular implementation
    tRed = get_max((0.759 * red) + (0.398 * green) + (0.194 * blue))
    tGreen = get_max((0.676 * red) + (0.354 * green) + (0.173 * blue))
    tBlue = get_max((0.524 * red) + (0.277 * green) + (0.136 * blue))

    if value == 1:
        tRed = get_max((0.759 * red) + (0.398 * green) + (0.194 * blue))
        tGreen = get_max((0.524 * red) + (0.277 * green) + (0.136 * blue))
        tBlue = get_max((0.676 * red) + (0.354 * green) + (0.173 * blue))
    if value == 2:
        tRed = get_max((0.676 * red) + (0.354 * green) + (0.173 * blue))
        tGreen = get_max((0.524 * red) + (0.277 * green) + (0.136 * blue))
        tBlue = get_max((0.524 * red) + (0.277 * green) + (0.136 * blue))

    # Return sepia color
    return tRed, tGreen, tBlue, alpha


# Return the color average
def color_average(image, i0, j0, i1, j1):
    # Colors
    red, green, blue, alpha = 0, 0, 0, 255

    # Get size
    width, height = image.size

    # Check size restrictions for width
    i_start, i_end = i0, i1
    if i0 < 0:
        i_start = 0
    if i1 > width:
        i_end = width

    # Check size restrictions for height
    j_start, j_end = j0, j1
    if j0 < 0:
        j_start = 0
    if j1 > height:
        j_end = height

    # This is a lazy approach, we discard half the pixels we are comparing
    # This will not affect the end result, but increase speed
    count = 0
    for i in range(i_start, i_end - 2, 2):
        for j in range(j_start, j_end - 2, 2):
            count += 1
            p = get_pixel(image, i, j)
            red, green, blue = p[0] + red, p[1] + green, p[2] + blue

    # Set color average
    red /= count
    green /= count
    blue /= count

    # Return color average
    return int(red), int(green), int(blue), alpha


# Convert an image to sepia
def convert_sepia(image):
    # Get size
    width, height = image.size

    # Create new Image and a Pixel Map
    new = create_image(width, height)
    pixels = new.load()

    # Convert each pixel to sepia
    for i in range(0, width, 1):
        for j in range(0, height, 1):
            p = get_pixel(image, i, j)
            pixels[i, j] = get_sepia_pixel(p[0], p[1], p[2], 255)

    # Return new image
    return new


def transformImages():
    for i in range(9):
        val = 42 + i
        img = Image.open('normalPics/img'+str(val)+'.jpg')
        img = img.resize((40, 40), Image.ANTIALIAS)
        img.save('normalPics/img'+str(val)+'.jpg')
        new = convert_sepia(img)
        save_image(new, 'sepiaPics/sepia' + str(val) + '.jpg')
