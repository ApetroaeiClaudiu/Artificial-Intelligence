import numpy
from PIL import Image, ImageDraw

def getMatrix():
    totalMatrix = []
    # POZE NORMALE
    for i in range(50):
        val = i + 1
        image = Image.open('normalPics/img' + str(val) + '.jpg','r')
        width, height = image.size
        pixel_values = list(image.getdata())
        if image.mode == 'RGBA':
            channels = 4
        elif image.mode == 'RGB':
            channels = 3
        elif image.mode == 'L':
            channels = 1
        else:
            print("Unknown mode: %s" % image.mode)
            print(i)
            return None
        pixel_values = numpy.array(pixel_values).reshape((width, height, channels))
        # aray de 40 x 40 x 3
        onePicValues = []
        for i in range(len(pixel_values)):
            for j in range(len(pixel_values)):
                onePicValues.append(pixel_values[i][j][0]-127)
                onePicValues.append(pixel_values[i][j][1]-127)
                onePicValues.append(pixel_values[i][j][2]-127)
        onePicValues.append(1)
        totalMatrix.append(onePicValues)

    #POZE SEPIA
    for i in range(50):
        val = i + 1
        image = Image.open('sepiaPics/sepia' + str(val) + '.jpg', 'r')
        width, height = image.size
        pixel_values = list(image.getdata())
        if image.mode == 'RGB':
            channels = 3
        elif image.mode == 'L':
            channels = 1
        else:
            print("Unknown mode: %s" % image.mode)
            return None
        pixel_values = numpy.array(pixel_values).reshape((width, height, channels))
        # aray de 40 x 40 x 3
        onePicValues = []
        for i in range(len(pixel_values)):
            for j in range(len(pixel_values)):
                onePicValues.append(pixel_values[i][j][0]-127)
                onePicValues.append(pixel_values[i][j][1]-127)
                onePicValues.append(pixel_values[i][j][2]-127)
        onePicValues.append(0)
        totalMatrix.append(onePicValues)
    return totalMatrix

