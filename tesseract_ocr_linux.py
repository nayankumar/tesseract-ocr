# import packages
from PIL import Image
import pytesseract
import os

# set working directory where your image files are
os.chdir("/home/nayan/Desktop/Codes Repository/OCR/Images")

# read black and white background image with PIL package
image_bw = Image.open("image_bw.png")

# extract text from image
print(pytesseract.image_to_string(image_bw))

''' Outptut

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

''' Outptut

'''

# read color image with PIL package
image_cl2 = Image.open("image_cl2.png")

# extract text from image
# if you have installed all the languages pack you will get different text than the original one
print(pytesseract.image_to_string(image_cl2))

''' Outptut

Sain Ae YEXTay eheer
kesseVash Beriormonce
MNSIaSkdncahwhite
background.

'''