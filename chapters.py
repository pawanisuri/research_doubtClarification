import os
from PyPDF2 import PdfFileReader, PdfFileWriter,PdfFileMerger
 
 
def pdf_splitter(path,spage,epage):
    fname = os.path.splitext(os.path.basename(path))[0]
 
    pdf = PdfFileReader(path)
    for page in range(spage,epage):
        pdf_writer = PdfFileWriter()
        # pdf_merger = PdfFileMerger()
        pdf_writer.addPage(pdf.getPage(page))
        output_filename = '{}_chaperts.pdf'.format(
            fname)
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)
        # merger = PdfFileMerger()
        # merger.append(PdfFileReader(file(x, 'rb')))
        # merger.write("document-output.pdf")

        print('Created: {}'.format(output_filename))
 
if __name__ == '__main__':
    path = 'Introduction_to_Software_Engineering.pdf'
    spage=12
    epage=17
    pdf_splitter(path,spage,epage)  