
import PyPDF2
import os.path

# Author: MasterWard
# Merges File 1 and File 2 together

def PDFmerge(pdfs, output): 
    # creating pdf file merger object
    pdfMerger = PyPDF2.PdfFileMerger()
    
    # appending pdfs one by one
    for pdf in pdfs:
        try:
            with open(pdf, 'rb') as f:
                temp = pdfMerger.id_count
                pdfMerger.append(f)
               # writing combined pdf to output pdf file
                with open(output, 'wb') as f:
                    pdfMerger.write(f) # Writing the File
                    print("ID: " + pdfMerger.id_count)
                    print("Number of pages " + len(pdfMerger.pages))
                    print("Number of Bookmarks " + len(pdfMerger.bookmarks))
                    print("Number of Destinations " + len(pdfMerger.named_dests))
        except IOError:
            print(pdf + " cannot be found")

def main():
    # pdf files to merge
    pdfs = ['First File.pdf', 'Second File.pdf']

    # output pdf file name
    output = 'Output File.pdf'

    # calling pdf merge function
    PDFmerge(pdfs, output)


if __name__ == "__main__":
    # calling the main function
    main()
