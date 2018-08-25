# tesseract-ocr
Text Extraction from Black and White Images

Useful Links:
	https://github.com/tesseract-ocr/tesseract/wiki
	
How it works:
	https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/33418.pdf
	
	
#==============================================================================
#==============================================================================
#				PYTHON
#==============================================================================
#==============================================================================
	
     
       
	
#===================
#	WINDOWS 10
#===================

Steps:

	1. Download tesseract setup [tesseract-ocr-setup-3.05.02-20180621.exe] from 		
	   https://github.com/UB-Mannheim/tesseract/wiki
	   
    2. Install the setup [It will take time if you select to install all languages]
	
	3. Install Pillow package [pip install pillow]
	
	4. Install pytesseract package [pip install pytesseract]
	
	5. Include tesseract installation path to path environment variable, in my case it is
	   C:\Program Files (x86)\Tesseract-OCR
	   
	6. Create new environment variable TESSDATA_PREFIX and set it to 
	   C:\Program Files (x86)\Tesseract-OCR\tessdata
	   
	7. Now run tesseract_ocr_windows.py file
	   
	   
Package Version:  

	python - 2.7.15 
	tesseract - 3.05.02
	pytesseract - 0.2.4
	pillow - 5.1.0



#=======================================
#	LINUX - Ubuntu 18.04 [Bionic Bever]
#=======================================

Steps:

	1. Install tesseract-ocr on linux by sudo apt install tesseract-ocr, sudo apt install  
	   libtesseract-dev
		a. If you want to install all the languages and scripts available by tesseract-ocr do  
		   sudo apt install tesseract-ocr-all
	
	2. Install Pillow package [pip install pillow]
	
	3. Install pytesseract package [pip install pytesseract]
	
	4. Now run tesseract_ocr_linux.py file
	
Package Version:  

	python - 2.7.15rc1 
	tesseract - 4.0.0-beta.1
	pytesseract - 0.2.4
	pillow - 5.2.0

	
	
#==============================================================================
#==============================================================================
#				R
#==============================================================================
#==============================================================================

Steps:  

  1. Open R Studio, install tesseract package by install.packages("tesseract") then run 
	   tesseract_ocr.R file
	
Package Version:

	R - 3.5.0 (2018-04-23) -- "Joy in Playing"
	tesseract - 2.3
  
#==============================================================================
#==============================================================================
#			Limitation
#==============================================================================
#==============================================================================

Tesseract-OCR works well in case of black and white images. It will extract all the text perfectly.  
When it comes to colorful images it does not work well. Text extraction will be imperfect.
