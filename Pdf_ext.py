import PyPDF2


pdfFileObj = open('example.pdf', 'rb')
  
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print(pdfReader.numPages)