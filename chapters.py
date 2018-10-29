import os
from PyPDF2 import PdfFileReader, PdfFileWriter,PdfFileMerger
 
 
def pdf_splitter(path,spage,epage):
    print(path)
    pathToOriginalPDF=path+'.pdf'
    pathTochapterPDF=path+'chapter.pdf'
    # exists = os.path.isfile(pathTochapterPDF)
    if os.path.exists(pathTochapterPDF):
        # os.remove(pathTochapterPDF)
        
        print("same name book is there")
    else:     
        # if exists:
        #     print("File is existing")
        #     NewchapterPDF=path+'AppendChapter.pdf'
        #     fname = os.path.splitext(os.path.basename(pathToOriginalPDF))[0]
        #     outputStream = open(NewchapterPDF, "wb")
        #     pdf = PdfFileReader(pathToOriginalPDF)
        #     pdf_writer = PdfFileWriter()
        #     merger = PdfFileMerger()
            
        #     for page in range(spage,epage):
        #         print(pdf.getPage(page))
        #         pdf_merger = PdfFileMerger()
        #         pdf_writer.addPage(pdf.getPage(page))
        #         pdf_writer.write(outputStream)

        #     pdf = PdfFileReader(NewchapterPDF)   
        #     outputStream = open(pathTochapterPDF, "wb") 
        #     for page in range(spage,epage):
        #         print(pdf.getPage(page))
        #         pdf_merger = PdfFileMerger()
        #         pdf_writer.addPage(pdf.getPage(page))
        #         pdf_writer.write(outputStream)    
        # else:
        # print("hello file is not existing")
        fname = os.path.splitext(os.path.basename(pathToOriginalPDF))[0]
        outputStream = open(pathTochapterPDF, "wb")
        pdf = PdfFileReader(pathToOriginalPDF)
        pdf_writer = PdfFileWriter()
        merger = PdfFileMerger()
        for sp in spage:
            for ep in epage:    
                for page in range(sp,ep):
                    print(pdf.getPage(page))
                    pdf_merger = PdfFileMerger()
                    pdf_writer.addPage(pdf.getPage(page))
                    pdf_writer.write(outputStream)
                break 
                    # output_filename = '{}_chaperts.pdf'.format(
                    #     fname)
                    # with open(output_filename, 'wb') as out:
                    #     pdf_writer.write(out)
                
                    # merger.append(PdfFileReader(file(pdf_writer.addPage(pdf.getPage(page)), 'rb')))
                    # merger.write("document-output.pdf")
    return("Success")
                    # print('Created: {}'.format(output_filename))
                # outputStream.close()
# if __name__ == '__main__':
#     path = 'McGrawHill - Machine Learning -Tom Mitchell'
#     spage=[14]
#     epage=[23]
#     pdf_splitter(path,spage,epage)  