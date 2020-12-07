import class_set
import constant
import pdfminer
import pdfminer.high_level
import pdfminer.layout
import excel_output
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from datetime import datetime


class Pdf2Excel():
    def __init__(self):
        self.gladefile = "./glade/pdf2excel_gui.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("window1")
        self.convert_button = self.builder.get_object("button_convert_file")
        self.convert_button.set_sensitive(False)
        self.create_textview_log()
        self.window.show()

    def create_textview_log(self):
        self.text_buffer = Gtk.TextBuffer()
        self.textview_log = self.builder.get_object("textview_log")
        self.textview_log.set_buffer(self.text_buffer)
        self.textview_log.set_editable(False)

    def on_button_quit_clicked(self, widget, data=None):
        print("Quit with cancel")
        Gtk.main_quit()

    # button 'convert file' convert selected .pdf customs data to its Excel file
    # format
    def on_button_convert_file_clicked(self, widget, data=None):
        log_content = "converting selected file:" + self.file_selected
        self.log_buffer(log_content)
#        custom_pdf_2_txt.pdf_2_txt(self.file_selected)
        self.pdf_2_txt(self.file_selected)
        self.convert_button.set_sensitive(False)

    # button 'select file' brings up a file chooser dialog
    def on_button_select_file_clicked(self, widget, data=None):
        self.fcd = Gtk.FileChooserDialog(title="選取檔案...",
                   parent=None,
                   action=Gtk.FileChooserAction.OPEN)
        self.fcd.add_button(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL)
        self.fcd.add_button(Gtk.STOCK_OPEN, Gtk.ResponseType.OK)
        self.fcd.set_default_size(300, 200)
        self.create_filechooser_filter()
        self.response = self.fcd.run()
        if self.response == Gtk.ResponseType.OK:
            self.file_selected = self.fcd.get_filename()
            log_content = "Selected file path: " + self.file_selected
            self.log_buffer(log_content)
            self.convert_button.set_sensitive(True)
            self.fcd.destroy()
        else:
            self.fcd.destroy()

    # added a file filter to the file chooser dialog
    def create_filechooser_filter(self):
        pdf_filter = Gtk.FileFilter()
        pdf_filter.add_mime_type("application/pdf")
        pdf_filter.set_name("*.pdf 檔案")
        self.fcd.add_filter(pdf_filter)

        txt_filter = Gtk.FileFilter()
        txt_filter.add_mime_type("text/plain")
        txt_filter.set_name("*.txt 文字檔案")
        self.fcd.add_filter(txt_filter)

        excel_filter = Gtk.FileFilter()
        excel_filter.add_mime_type("application/vnd.ms-excel")
        excel_filter.add_mime_type("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        excel_filter.set_name("*.xlsx Excel 檔案")
        self.fcd.add_filter(excel_filter)

        any_filter = Gtk.FileFilter()
        any_filter.add_pattern("*.*")
        any_filter.set_name("所有檔案")
        self.fcd.add_filter(any_filter)

    # log utility, attach time stamp to log_content
    def log_buffer(self, log_content):
        datetimeObj = datetime.now()
        #timestamp = str(datetimeObj.year) + "/" + str(datetimeObj.month) + "/" + str(datetimeObj.day) \
        #            + " " + str(datetimeObj.hour) + ":" + str(datetimeObj.minute) + ":" + str(datetimeObj.second) \
        #            + ">>> "
        timestamp = datetimeObj.strftime("%Y/%m/%d %H:%M:%S")
        log_content = timestamp + " >>> " + log_content
        buffer1 = self.text_buffer
        end_iter = buffer1.get_end_iter()
        buffer1.insert(end_iter, log_content + "\n")

    def pdf_2_txt(self, input_file):
        self.log_buffer("call pdf_2_txt() to do conversion")
        textoutput_file = ""            # text output file
        output_file = ""                # output csv file
        # declare new lists
        tax_bill_list = []              # 稅單號碼
        declaration_form_list = []      # 報單號碼
        tax_ID_list = []                # 納稅義務人統一標號
        tax_amount_list = []            # 金額

        first_page = True               # end of Tax_ID of the 1st page differs from
                                        # the rest pages
        tax_bill_or_not = True          # pdfminer 產出的文字檔，"稅單號碼""與"報單號碼" 合併在同一欄位

        # creating counters to ensure all information is consistent
        tax_bill_count = 0
        decl_form_count = 0
        tax_ID_count = 0
        tax_amount_count = 0
        # initializing field entries to mark states of a state machine
        tax_bill_entry = False          # 稅單資料輸入
        decl_form_entry = False         # 報單資料輸入
        tax_ID_entry = False            # 統一編號輸入
        tax_amount_entry = False        # 報單金額輸入
        es = class_set.entry_setting(tax_bill_entry, decl_form_entry, tax_ID_entry, tax_amount_entry)

        self.log_buffer("\t輸入彙總稅單清單名稱(pdf): " + input_file)
        if input_file != "":
            ifObj = open(input_file, "rb")
        else:
            self.log_buffer("\t請選取彙總稅單清單名稱!")
            return()

        stripped_file_name = input_file[:len(input_file)-3]
        # intermediate .text file
        if textoutput_file == "":
            textoutput_file = stripped_file_name + "text"
        self.log_buffer("\t彙總稅單文字內容(text): " + textoutput_file)
        if os.path.isfile("./"+ textoutput_file):
            os.remove("./"+ textoutput_file)
        tfObj = open(textoutput_file, "wb")

        # intermediate .txt of tab seperated file format
        if output_file == "":
            output_file = stripped_file_name + "txt"
        self.log_buffer("\t彙總稅單清單轉出名稱(tab separated): " + output_file)
        ofObj = open(output_file, "w", encoding="utf-8")

        # setup pdfminer operation
        all_texts = None
        detect_vertical = None
        word_margin = None
        char_margin = None
        line_margin = None
        boxes_flow = None
        strip_control = False
        output_type = 'text'
        layoutmode = 'normal'
        laparams = pdfminer.layout.LAParams()
        for param in ("all_texts", "detect_vertical", "word_margin", "char_margin", "line_margin", "boxes_flow"):
                paramv = locals().get(param, None)
                if paramv is not None:
                    setattr(laparams, param, paramv)
        pdfminer.high_level.extract_text_to_fp(ifObj, tfObj, **locals())
        tfObj.close()

        # __debug__ won't be executed unless -O is set when launching python
        if __debug__ is False:
            dbgFileObj = open("debug_output.txt", "w", encoding="utf-8")

        tfObj = open(textoutput_file, "r", encoding="utf-8")
        print_flag = False
        # reading input file line-by-line
        tfStr = tfObj.readline()

        while tfStr:
            if tfStr.strip('\n') == constant.FILE_HEADER:
                # 彙總稅單稅單清單
                if __debug__ is False:
                    print("File Header: ", tfStr.strip('\n'))
            elif tfStr.strip('\n') == constant.BEGINNING_DECLARATION_ID:
                # 報單號碼
                print_flag = True
                tax_bill_entry, decl_form_entry, tax_ID_entry, tax_amount_entry = \
                    es.clear_current_setting()
                tax_bill_entry = True
                es.set_current_entry(tax_bill_entry, decl_form_entry, tax_ID_entry, tax_amount_entry)
                if __debug__ is False:
                    print("Beginning declaration ID: ", tfStr.strip('\n'))
            elif tfStr.strip('\n') == constant.BEGINNING_TAX_ID_COLUMN:
                # also END_DECLARATION_ID
                # 納稅義務人統編
                print_flag = True
                tax_bill_entry, decl_form_entry, tax_ID_entry, tax_amount_entry = \
                    es.clear_current_setting()
                tax_ID_entry = True
                es.set_current_entry(tax_bill_entry, decl_form_entry, tax_ID_entry, tax_amount_entry)
                if __debug__ is False:
                    print("Tax ID: ", tfStr.strip('\n'))
            elif tfStr.strip('\n') == constant.BEGINNING_AMOUNT_COLUMN:
                # 金額
                print_flag = True
                tax_bill_entry, decl_form_entry, tax_ID_entry, tax_amount_entry = \
                    es.clear_current_setting()
                tax_amount_entry = True
                es.set_current_entry(tax_bill_entry, decl_form_entry, tax_ID_entry, tax_amount_entry)
                if __debug__ is False:
                    print("Amount: ", tfStr.strip('\n'))
            elif tfStr.strip('\n') == constant.END_AMOUNT_COLUMN_P1:
                print_flag = True
                tax_bill_entry, decl_form_entry, tax_ID_entry, tax_amount_entry = \
                    es.clear_current_setting()
                if __debug__ is False:
                    dbgFileObj.write("<<<<製表日期>>>>\n")
            elif tfStr[:2] == constant.END_TAX_ID_P2:
                print_flag = True
                tax_bill_entry, decl_form_entry, tax_ID_entry, tax_amount_entry = \
                    es.clear_current_setting()
                if __debug__ is False:
                    dbgFileObj.write("<<<<頁碼>>>>\n")
            elif tfStr.strip('\n') == constant.RECORD_COUNT:
                print_flag = True
                tax_bill_entry, decl_form_entry, tax_ID_entry, tax_amount_entry = \
                    es.clear_current_setting()
                if __debug__ is False:
                    dbgFileObj.write("<<<<總筆數>>>>\n")
            #
            # processing per state machine
            #
            valid_entry, tax_bill_entry, decl_form_entry, tax_ID_entry, tax_amount_entry = \
                es.get_current_setting()
            # state machine processing column entries
            if tax_bill_entry is True:
                if print_flag is True:
                    print_flag = False
                    if __debug__ is False:
                        dbgFileObj.write(tfStr)
                else:
                    if tfStr.strip('\n') != "":
                        if tax_bill_or_not is True:
                            tax_bill_list.append(tfStr.strip('\n'))
                            tax_bill_or_not = False
                        else:
                            declaration_form_list.append(tfStr.strip('\n'))
                            tax_bill_or_not = True
                        if __debug__ is False:
                            dbgFileObj.write(tfStr)
            elif tax_ID_entry is True:
                if print_flag is True:
                    print_flag = False
                    if __debug__ is False:
                        dbgFileObj.write(tfStr)
                else:
                    if tfStr.strip('\n') != "":
                        tax_ID_list.append(tfStr.strip('\n'))
                        if __debug__ is False:
                            dbgFileObj.write(tfStr)
            elif tax_amount_entry is True:
                if print_flag is True:
                    print_flag = False
                    if __debug__ is False:
                        dbgFileObj.write(tfStr)
                else:
                    if tfStr.strip('\n') != "":
                        tax_amount_list.append(tfStr.strip('\n'))
                        if __debug__ is False:
                            dbgFileObj.write(tfStr)

            tfStr = tfObj.readline()

        if __debug__ is False:
            dbgFileObj.write("tax_bill_list length:" + str(len(tax_bill_list)) + "\n")
            dbgFileObj.write("declaration_foㄋrm_list:" + str(len(declaration_form_list)) + "\n")
            dbgFileObj.write("tax_ID_list:" + str(len(tax_ID_list)) + "\n")
            dbgFileObj.write("tax_amount_llist:" + str(len(tax_amount_list)) + "\n")
        #
        # compose output file by combining the four lists collected in
        # the above statemachine
        #
        if len(tax_bill_list) == len(declaration_form_list) == len(tax_ID_list) == \
            len(tax_amount_list):
            for i in range(0, len(tax_bill_list)):
                combined_string = declaration_form_list[i] + "\t" + tax_bill_list[i] + \
                                "\t" + tax_ID_list[i] + "\t" + tax_amount_list[i] + "\n"
                ofObj.write(combined_string)
            excel_output.generate_excel_output(stripped_file_name, tax_bill_list, declaration_form_list, tax_ID_list, tax_amount_list)
            self.log_buffer("\t產出彙總稅單清單轉檔(.xslx):" + stripped_file_name + "xlsx")
        else:
            self.log_buffer("\tExcel 檔案產生失敗!ㄋ")

        if ifObj.closed is False:
            ifObj.close()

        if ofObj.closed is False:
            ofObj.close()

        if tfObj.closed is False:
            tfObj.close()

        if __debug__ is False:
            dbgFileObj.close()


if __name__ == "__main__":
    # create a new instance of Pdf2Excel()
    main = Pdf2Excel()
    Gtk.main()
