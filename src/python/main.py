from PyPDF2 import PdfFileWriter, PdfFileReader
import js2py

def read_pdf():
    filename = "Homework01.pdf"
    pdfFileObject = open(filename, 'rb')
    pdfReader = PdfFileReader(pdfFileObject)
    pageObject = pdfReader.getPage(0)
    print(pageObject.extractText())
    pdfFileObject.close()

def convert_to_malicious_pdf():
    filename = "Homework01.pdf"
    output = PdfFileWriter()
    input_pdf = PdfFileReader(open(filename, 'rb'))
    # go through page by page
    for page_number in range(input_pdf.getNumPages()):
        page = input_pdf.getPage(page_number)
        output.addPage(page )

    with open("MaliciousHomework1.pdf", 'wb') as file:
        #output.addJS("this.print({bUI:true,bSilent:false,bShrinkToFit:true});")
        maliciousJS = """app.alert({cMsg: 'Hello from PDF JavaScript', cTitle: 'Testing PDF JavaScript', nIcon: 3});"""
        outputMaliciousJS = js2py.eval_js(maliciousJS)
        output.addJS(maliciousJS)
        output.write(file)


def main():
    read_pdf()
    convert_to_malicious_pdf()
main()
