import PyPDF2

def read_pdf():
    filename = "Homework01.pdf"
    pdfFileObject = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
    pageObject = pdfReader.getPage(0)
    print(pageObject.extractText())
    pdfFileObject.close()

def convert_to_malicious_pdf():
    filename = "Homework01.pdf"
    pdfFileObject = open(filename, 'wb')
    pdfWriter = PyPDF2.PdfFileWriter(pdfFileObject)
    pageObj = pdfFileObject.addBlankPage(width = 200, height = 200)
    pdfWriter.addJS("this.print({bUI:true,bSilent:false,bShrinkToFit:true});")
    pdfFileObject.close()

def main():
    read_pdf()
    convert_to_malicious_pdf
    read_pdf()
main()