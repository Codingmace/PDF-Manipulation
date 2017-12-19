import PyPDF2
import os.path


def PDFmerge(pdfs, output): 
    # creating pdf file merger object
    pdfMerger = PyPDF2.PdfFileMerger()
    
    # appending pdfs one by one
    for pdf in pdfs:
        
        with open(pdf, 'rb') as f:
            temp = pdfMerger.id_count
           # pdfMerger.addBookmark("Holly", temp)
            pdfMerger.append(f)

    # writing combined pdf to output pdf file
    with open(output, 'wb') as f:
        pdfMerger.write(f)
        print(pdfMerger.id_count)
        print(len(pdfMerger.pages))
        print(len(pdfMerger.bookmarks))
        print(len(pdfMerger.named_dests))
        

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
