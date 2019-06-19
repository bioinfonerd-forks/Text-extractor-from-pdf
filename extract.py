import pytesseract 
from pdf2image import convert_from_path 
import time
from _thread import *
OMP_THREAD_LIMIT=4
def extract_text_pdf_ocr(pdf_path):
        text=''
        pages = convert_from_path(pdf_path, 100) 
        for page in pages: 
                text += str(pytesseract.image_to_string(page))
        return text
if __name__ == '__main__':
    start=time.time()
    text=extract_text_pdf_ocr('Arpita Bose cv.pdf') 
    end=time.time()
    print(end-start,'\n',text)
    
