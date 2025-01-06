#install pdf2docx first fro installing type "pip install pdf2docx" to terminal
#pip install PyMuPDf==1.24.14
#pip install fonttools==4.55.0
from pdf2docx import Converter # In This we are calling the pdf2docx 

path_pdf="hello.pdf" # name of pdf which we have to convert IT SHOULD BE IN A SAME FOLDER
path_docx ="new.docx" # write any name from ehich you want the docx 

cv = Converter(path_pdf)
cv.convert(path_docx,start=0,end=None) # all the pages should be in default format
cv.close()