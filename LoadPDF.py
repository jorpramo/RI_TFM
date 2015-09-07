from PyPDF2 import PdfFileWriter, PdfFileReader

input1 = PdfFileReader(open("C:/Users/jpradas/Documents/MASTER/TFM/code/data/pdf/myfile.pdf", "rb"))

print(input1.getNumPages())
print(input1.getDocumentInfo())
pagina=input1.getPage(3)
print(pagina.extractText().encode('utf-8').decode('cp1251').encode('utf-8'))

