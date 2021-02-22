
''' Add full path to not get confused '''
class JoinDirManager:
    def __init__(self, parent=None):
        self.parent = parent
        self.__current_file_info = None
        self.__files_tree_widget = self.parent.builder.get_object('JoinDirList')
        self.__files_tree_widget['displaycolumns'] = ('FoldNameColumn', 'PageSelectColumn')
        self.__current_file_info_widget = self.parent.builder.get_variable('current_file_info')
        self.__page_select_input_widget = self.parent.builder.get_variable('page_select_input')
        self.__selected_files = []

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, val):
        self.__parent = val

    def on_file_select(self, event):
        self.__selected_files = self.__files_tree_widget.selection()
        self.__current_file_info = PDFPageInfo(
            self.__files_tree_widget.item(self.__selected_files[0], 'values')[PDF_FILEPATH])
        self.__show_file_info()
        self.__show_selected_pages()

    def enter_page_selection(self, event):
        '''
        This medthod is called when the page selection input field loses focus
        i.e. when input is completed
        '''
        for f in self.__selected_files:
            file_data = self.__files_tree_widget.item(f, 'values')
            page_select = self.__page_select_input_widget.get()
            new_tuple = (file_data[PDF_FILENAME], page_select, file_data[PDF_FILEPATH], file_data[PDF_PAGES])
            self.__files_tree_widget.item(f, values=new_tuple)

    def __show_file_info(self):
        self.__current_file_info_widget.set(self.__current_file_info.pdf_info_string(concat_length=25))

    def __show_selected_pages(self):
        file_data = self.__files_tree_widget.item(self.__selected_files[0], 'values')
        self.__page_select_input_widget.set(file_data[PDF_PAGESELECT])

    def __get_join_files(self):
        return [self.__files_tree_widget.item(i)['values'] for i in self.__files_tree_widget.get_children()]

    def __parse_page_select(self, page_select):
        '''
        As this method deals with raw user input, there will have to be a whole lot of error checking
        built into this function at a later time. Really don't look forward to this… at all.
        '''
        for page_range in page_select.replace(' ', '').split(','):
            if '-' in page_range:
                range_list = page_range.split('-')
                yield tuple(sorted((int(range_list[0])-1, int(range_list[1]))))
            else:
                yield tuple(sorted((int(page_range)-1, int(page_range))))

    def add_file(self):
        add_filepaths = self.parent.get_file_dialog(
            func=filedialog.askopenfilenames,
            widget_title='Choose PDFs to Add…'
        )
        if add_filepaths:
            for filepath in list(add_filepaths):
                print(os.path.abspath(filepath)) 
                filename = os.path.basename(filepath)
                file_info = PDFPageInfo(filepath)
                file_data = (filename, '', filepath, file_info.pages)
                self.__files_tree_widget.insert('', 'end', values=file_data)

    def save_as(self):
        if len(self.__get_join_files()) > 0:
            save_filepath = self.parent.get_file_dialog(
                func=filedialog.asksaveasfilename, widget_title='Save Joined PDF to…')
            if save_filepath:
                merger = PdfFileMerger()
                for f in self.__get_join_files():
                    if not f[PDF_PAGESELECT]:
                        merger.append(fileobj=open(f[PDF_FILEPATH], 'rb'))
                    else:
                        for page_range in self.__parse_page_select(str(f[PDF_PAGESELECT])):
                            merger.append(fileobj=open(f[PDF_FILEPATH], 'rb'), pages=page_range)
                with open(save_filepath, 'wb') as out_pdf:
                    merger.write(out_pdf)
                self.parent.save_success(status_text=JOIN_FILE_SUCCESS.format(os.path.basename(save_filepath)))

    def move_up(self):
        selected_files = self.__selected_files
        first_idx = self.__files_tree_widget.index(selected_files[0])
        parent = self.__files_tree_widget.parent(selected_files[0])
        if first_idx > 0:
            for f in selected_files:
                swap_item = self.__files_tree_widget.prev(f)
                new_idx = self.__files_tree_widget.index(swap_item)
                self.__files_tree_widget.move(f, parent, new_idx)

    def move_down(self):
        selected_files = list(reversed(self.__selected_files))
        last_idx = self.__files_tree_widget.index(selected_files[0])
        parent = self.__files_tree_widget.parent(selected_files[0])
        last_idx_in_widget = self.__files_tree_widget.index(self.__files_tree_widget.get_children()[-1])
        if last_idx < last_idx_in_widget:
            for f in selected_files:
                swap_item = self.__files_tree_widget.next(f)
                own_idx = self.__files_tree_widget.index(f)
                new_idx = self.__files_tree_widget.index(swap_item)
                self.__files_tree_widget.move(f, parent, new_idx)

    def remove_file(self):
        for f in self.__selected_files:
            self.__files_tree_widget.detach(f)

