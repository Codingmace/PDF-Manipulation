
class BgTabManager:
    def __init__(self, parent=None):
        self.parent = parent
        self.__source_filepath = None
        self.__bg_filepath = None
        self.__source_file_info = None
        self.__bg_file_info = None
        self.__bg_pdf_pages = None
        self.__source_file_info_widget = self.parent.builder.get_variable('source_file_info')
        self.__bg_file_info_widget = self.parent.builder.get_variable('bg_file_info')
        self.__bg_command = self.parent.builder.get_variable('bg_command')
        self.__bg_only_first_page = self.parent.builder.get_variable('bg_only_first_page')
        self.__bg_button_label = self.parent.builder.get_variable('bg_options_bg_button')
        self.__only_first_button_label = self.parent.builder.get_variable('bg_options_only_first_button')
        self.__bg_command.set('BG')

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, val):
        self.__parent = val

    def choose_source_file(self):
        choose_source_file = self.parent.get_file_dialog(
            func=filedialog.askopenfilename, widget_title='Choose Source PDF ...')
        if choose_source_file:
            self.__source_filepath = choose_source_file
            self.__source_file_info = PDFPageInfo(self.__source_filepath)
            self.__show_source_file_info()

    def choose_bg_file(self):
        choose_bg_file = self.parent.get_file_dialog(
            func=filedialog.askopenfilename, widget_title='Choose Background PDF ...')
        if choose_bg_file:
            self.__bg_filepath = choose_bg_file
            self.__bg_file_info = PDFPageInfo(self.__bg_filepath)
            self.__show_bg_file_info()

    def __show_source_file_info(self):
        self.__source_file_info_widget.set(self.__source_file_info.pdf_info_string(concat_length=80))

    def __show_bg_file_info(self):
        self.__bg_file_info_widget.set(self.__bg_file_info.pdf_info_string(concat_length=80))

    def choose_stamp_option(self):
        self.__only_first_button_label.set('Apply stamp to only the first page')
        self.__bg_button_label.set('Choose Stamp ...')

    def choose_bg_option(self):
        self.__only_first_button_label.set('Apply background to only the first page')
        self.__bg_button_label.set('Choose Background ...')

    def save_as(self):
        save_filepath = self.parent.get_file_dialog(func=filedialog.asksaveasfilename, widget_title='Save New PDF to ...')
        if self.__source_filepath and self.__bg_filepath:
            out_pdf = PdfFileWriter()
            command = self.__bg_command.get()
            with open(self.__source_filepath, "rb") as source_pdf_stream, \
                    open(self.__bg_filepath, "rb") as bg_pdf_stream:
                for p in range(self.__source_file_info.pages):
                    # new PdfFileReader instances needed for every page merged. See here:
                    # https://github.com/mstamy2/PyPDF2/issues/100#issuecomment-43145634
                    source_pdf = PdfFileReader(source_pdf_stream)
                    bg_pdf = PdfFileReader(bg_pdf_stream)
                    if not self.__bg_only_first_page.get() or (self.__bg_only_first_page.get() and p < 1):
                        if command == 'STAMP':
                            top_page = bg_pdf.getPage(0)
                            bottom_page = source_pdf.getPage(p)
                        elif command == 'BG':
                            top_page = source_pdf.getPage(p)
                            bottom_page = bg_pdf.getPage(0)
                        bottom_page.mergePage(top_page)
                    else:
                        bottom_page = source_pdf.getPage(p)
                    out_pdf.addPage(bottom_page)
                with open(save_filepath, "wb") as out_pdf_stream:
                    out_pdf.write(out_pdf_stream)
            self.parent.save_success(status_text=BG_FILE_SUCCESS.format(os.path.basename(save_filepath)))
