# importing required modules
import PyPDF2
from PyPDF2 import PdfFileWriter, PdfFileReader

def PDFmerge(pdfs, output):
    # creating pdf file merger object
    pdfMerger = PyPDF2.PdfFileMerger()
 
    # existing_pdf = PdfFileReader("%sOutput.pdf" % (splittedName))
    # output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
    # pageNo=existing_pdf.getNumPages()
    # print(pageNo)
    # if(pageNo>0):
    # appending pdfs one by one
    for pdf in pdfs:
        print(pdf)
        with open(pdf, 'rb') as f:
            pdfMerger.append(f)
 
    # writing combined pdf to output pdf file
    with open(output, 'wb') as f:
        pdfMerger.write(f)

# To create pdfs for chapters
def createPDF(intialPDF,startPage,endPage):
    inputpdf = PdfFileReader(open(intialPDF, "rb"))
    splittedName=intialPDF.rsplit('.', 1)[0]
    pages=endPage-startPage
    index=0
    pdf=[None]*pages
    for i in range(startPage,endPage):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        with open("%s%s.pdf" % (splittedName,i), 'wb') as outputStream:
            output.write(outputStream) 
            pdf[index]="%s%s.pdf" % (splittedName,i)
            output="%sOutput.pdf" % (splittedName)
                # print(pdf[index])
            index=index+1
           
    PDFmerge(pdf,output)
    
createPDF("Introduction_to_Software_Engineering.pdf",26,29)            
# def PDFmerge(pdfs, output):
#     # creating pdf file merger object
#     pdfMerger = PyPDF2.PdfFileMerger()
 
#     # appending pdfs one by one
#     for pdf in pdfs:
#         with open(pdf, 'rb') as f:
#             pdfMerger.append(f)
 
#     # writing combined pdf to output pdf file
#     with open(output, 'wb') as f:
#         pdfMerger.write(f)
 
# def main():
#     # pdf files to merge
# pdfs = ['output.pdf', 'ccc.pdf']
 
#     # output pdf file name
# output  = 'combined_example.pdf'
 
#     # calling pdf merge function
# PDFmerge(pdfs = pdfs, output = output)
 
# if __name__ == "__main__":
#     # calling the main function
#     main()