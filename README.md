##Text extractor from pdf##
Required Packages:
	
	-->  python 3.x

	--> pdf2image

	--> pytesseract



Installing Packages:

pdf2image:


	--> sudo apt install poppler-utils
	--> pip install pdf2image

pytesseract:


	-->pip install pytesseract   
		(or)
	-->pip install -U git+https://github.com/madmaze/pytesseract.git
		(or)
	-->git clone https://github.com/madmaze/pytesseract.git 
	--> cd pytesseract && pip install -U .



Steps of Execution:

1.The method extract_text_pdf_ocr() takes input a pdf file and extract text from it and return the text.

2.In the first step it takes pdf file as input.

3.Next it convert the pdf file into images using pdf2image library.

4.Then it use tesseract to extract text from images and store it in a string variable

5.The above function takes ~1.4 sec per page to convert it to image and extract text from it.

6.The function return an string variable contains the text.

7. Tesseract 4 also uses up to four CPU threads while processing a page, so it will be faster

8. It should enabled using OMP_THREAD_LIMIT
	


