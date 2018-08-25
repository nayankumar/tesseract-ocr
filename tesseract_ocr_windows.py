# import packages
from PIL import Image
import pytesseract
import os

# set working directory where your image files are
os.chdir("D:\\Codes Repository\\AI_ML\\OCR\\Images")

# read black and white background image with PIL package
image_bw = Image.open("image_bw.png")

# extract text from image
print(pytesseract.image_to_string(image_bw))

''' Output

Sample text to check
tesseract performance
in black and white
background.

'''

# read color image with PIL package
image_cl1 = Image.open("image_cl1.png")

# extract text from image
# you will not get any text from this image as background and text color are similar
print(pytesseract.image_to_string(image_cl1))

''' Output

'''

# read color image with PIL package
image_cl2 = Image.open("image_cl2.png")

# extract text from image
# you will see that complete text is not extracted, there is an issue with tesseract word
print(pytesseract.image_to_string(image_cl2))

''' Output

Sample Text to check
’resserac’r performance
in black and white
background.

'''


#-----------------------------------------------------------------------#
#-----------------------------------------------------------------------#
# Read images and convert them into grey scale and then apply tesseract #
#-----------------------------------------------------------------------#
#-----------------------------------------------------------------------#

# read black and white background image with PIL package
image_bw = Image.open("image_bw.png").convert('L')

# extract text from image
print(pytesseract.image_to_string(image_bw))

''' Output

Sample text to check
tesseract performance
in black and white
background.

'''

# read color image with PIL package
image_cl1 = Image.open("image_cl1.png").convert('L')

# extract text from image
# you will not get any text from this image as background and text color are similar
print(pytesseract.image_to_string(image_cl1))

''' Output

'''

# read color image with PIL package
image_cl2 = Image.open("image_cl2.png").convert('L')

# extract text from image
# output is different when we have converted image to black and white
print(pytesseract.image_to_string(image_cl2))

''' Output

backg round.

'''