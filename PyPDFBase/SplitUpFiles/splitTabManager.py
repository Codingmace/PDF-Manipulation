

class SplitTabManager:
    '''Manager class for the Split Tab

    An instance of this class manages all aspects of the Split Tab in the calling `PyPDFBuilderApplication` instance

    Args:
        parent (PyPDFBuilderApplication): Application that created the instance and that contains the Split Tab.
    '''

    def __init__(self, parent=None):
        self.parent = parent
        self.__split_filepath = None
        self.__split_file_info = None
        self.__split_file_info_widget = self.parent.builder.get_variable('split_file_info')

    @property
    def parent(self):
        '''PyPDFBuilderApplication: Application that created the instance and that contains the Split Tab.'''
        return self.__parent

    @parent.setter
    def parent(self, val):
        self.__parent = val

    def open_file(self):
        choose_split_file = self.parent.get_file_dialog(
            func=filedialog.askopenfilename, widget_title='Choose PDF to Split ...')
        if choose_split_file:
            self.__split_filepath = choose_split_file
            self.__split_file_info = PDFInfo(self.__split_filepath)
            self.__show_file_info()

    def __show_file_info(self):
        self.__split_file_info_widget.set(self.__split_file_info.pdf_info_string())

    def save_as(self):
        if self.__split_filepath:
            basepath = os.path.splitext(self.__split_filepath)[0]
            # in spite of discussion here https://stackoverflow.com/a/2189814
            # we'll just go the lazy way to count the number of needed digits:
            num_length = len(str(abs(self.__split_file_info.pages)))
            in_pdf = PdfFileReader(open(self.__split_filepath, "rb"))
            for p in range(self.__split_file_info.pages):
                output_path = f"{basepath}_{str(p+1).rjust(num_length, '0')}.pdf"
                out_pdf = PdfFileWriter()
                out_pdf.addPage(in_pdf.getPage(p))
                with open(output_path, "wb") as out_pdf_stream:
                    out_pdf.write(out_pdf_stream)
            self.parent.save_success(status_text=SPLIT_FILE_SUCCESS.format(os.path.dirname(self.__split_filepath)))
