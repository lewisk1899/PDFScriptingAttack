from PyPDF2 import PdfFileWriter

file = PdfFileWriter()

file.addBlankPage(
    width= 200,
    height= 200
)
file.addBlankPage(
    width=100,
    height=500
)

output = open('blankPdf.pdf', 'wb')
file.write(output)