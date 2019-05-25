import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os
def extract_text_pdf_ocr(pdf_path,out_path):
    f = open(out_path, "a")  
    pages = convert_from_path(pdf_path, 500) 
    for page in pages: 
       
        text = str(pytesseract.image_to_string(page))
        text = text.replace('-\n', '')     
        f.write(text) 
    f.close() 
if __name__ == '__main__':
    pdf_path=input("Enter name of pdf file:")
    out_path=pdf_path.split('.')[0]
    extract_text_pdf_ocr(pdf_path,out_path)
   
