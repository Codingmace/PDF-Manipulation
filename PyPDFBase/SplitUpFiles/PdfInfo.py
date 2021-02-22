
''' ADJUST TO HAVE WAY MORE INFORMATION 
    Is related to the split class '''
class PDFInfo:
    '''File info class for PDF files.

    Instances of this class show information about PDF files that are being edited in
    PyPDF Builder.

    Args:
        filepath (str): Path to PDF File
    '''

    def __init__(self, filepath):
        self.__filepath = filepath

    @property
    def pages(self):
        '''int: Number of pages contained in PDF file'''
        with open(self.__filepath, 'rb') as in_pdf:
            pdf_handler = PdfFileReader(in_pdf)
            return pdf_handler.getNumPages()

    def concat_filename(self, max_length=35):
        '''Concatenate a filename to a certain length.

        Args:
            max_length (int): Maximum length of concatenated string (default: 35)

        Returns:
            str: Filename of PDFPageInfo-object concatenated to max length of `max_length`

        '''
        basename = os.path.basename(self.__filepath)
        concat_filename = f'{basename[0:max_length]}'
        if len(basename) > max_length:
            concat_filename += '...'
        return concat_filename

    def pdf_info_string(self, concat_length=35):
        '''Fetch a standard info-string about the PDFPageInfo-object.

        Args:
            concat_length (int): Maximum length of concatenated filename string (default: 35)

        Returns:
            str: Information in the format `Filename (pages)` of PDFPageInfo-object

        '''
        concat_filename = self.concat_filename(max_length=concat_length)
        return f'{concat_filename} ({self.pages} pages)'

