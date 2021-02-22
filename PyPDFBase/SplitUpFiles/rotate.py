
class RotateTabManager:
    def __init__(self, parent=None):
        self.parent = parent
        self.__rotate_filepath = None
        self.__rotate_file_info = None
        self.__rotate_file_info_widget = self.parent.builder.get_variable('rotate_file_info')
        self.__rotate_from_page_widget = self.parent.builder.get_variable('rotate_from_page')
        self.__rotate_to_page_widget = self.parent.builder.get_variable('rotate_to_page')
        self.__rotate_amount_widget = self.parent.builder.get_variable('rotate_amount')
        self.__do_page_extract_widget = self.parent.builder.get_variable('do_extract_pages')
        # Set default values. No idea how to avoid this using only the UI file, so I'm
        # breaking the MVC principle here.
        self.__rotate_amount_widget.set('NO_ROTATE')
        self.__rotate_from_page_widget.set('')
        self.__rotate_to_page_widget.set('')
        self.__do_page_extract_widget.set(True)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, val):
        self.__parent = val

    def open_file(self):
        chose_rotate_file = self.parent.get_file_dialog(
            func=filedialog.askopenfilename, widget_title='Choose PDF to Rotate...')
        if chose_rotate_file:
            self.__rotate_filepath = chose_rotate_file
            self.__rotate_file_info = PDFPageInfo(self.__rotate_filepath)
            self.__show_file_info()
            self.__show_rotate_pages()

    def __show_rotate_pages(self):
        self.__rotate_from_page_widget.set(1)
        self.__rotate_to_page_widget.set(self.__rotate_file_info.pages)

    def __show_file_info(self):
        self.__rotate_file_info_widget.set(self.__rotate_file_info.pdf_info_string())

    def save_as(self):
        page_range = (self.__rotate_from_page_widget.get()-1, self.__rotate_to_page_widget.get())
        save_filepath = self.parent.get_file_dialog(func=filedialog.asksaveasfilename, widget_title='Save New PDF to...')
        if self.__rotate_filepath:
            in_pdf = PdfFileReader(open(self.__rotate_filepath, "rb"))
            out_pdf = PdfFileWriter()
            for p in range(self.__rotate_file_info.pages):
                if p in range(*page_range):
                    if ROTATE_DEGREES[self.__rotate_amount_widget.get()] != 0:            
                        out_pdf.addPage(in_pdf.getPage(p).rotateClockwise(
                            ROTATE_DEGREES[self.__rotate_amount_widget.get()]))
                    else:
                        out_pdf.addPage(in_pdf.getPage(p))
                elif not self.__do_page_extract_widget.get():
                    out_pdf.addPage(in_pdf.getPage(p))
            with open(save_filepath, "wb") as out_pdf_stream:
                out_pdf.write(out_pdf_stream)
            self.parent.save_success(status_text=ROTATE_FILE_SUCCESS.format(os.path.basename(save_filepath)))
