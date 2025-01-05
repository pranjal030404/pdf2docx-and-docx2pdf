# install docx2pdf by typing "pip install docx2pdf " This will help you to convert 
from docx2pdf import convert # importing docx2pdf


path_doc="MySQL.docx" # insert the docx name which you want to convert , docx should be in same folder 
path_pdf ="hello.pdf" # write the name of the pdf by which you want to convert and save 

convert(path_doc,path_pdf) # This function is mainally converting the docx to pdf 