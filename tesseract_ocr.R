# set working directory where images resides
setwd("D:\\Codes Repository\\AI_ML\\OCR\\Images")

# load required library
library(tesseract)

# read image
image_bw <- tesseract::ocr("image_bw.png", engine = tesseract("eng"))
cat(image_bw)

# Outptut
# Sample text to check
# tesseract performance
# in black and white
# background.


# read image
image_cl1 <- tesseract::ocr("image_cl1.png", engine = tesseract("eng"))
cat(image_cl1)

# Outptut
# >I\I\I\I\I\I\I\
# 
# §§®???§®§§§9§§
# 
# I gmmqa W!
#   
# W :W: 2"":


# read image
image_cl2 <- tesseract::ocr("image_cl2.png", engine = tesseract("eng"))
cat(image_cl2)

# Outptut
# Sample Text to check
# 'resserac'r performance
# in black and white
# background.