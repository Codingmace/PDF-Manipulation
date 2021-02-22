#!/usr/bin/python

import os
import sys
import appdirs
import json
from pathlib import Path as plPath
from operator import itemgetter
from settings import *

import UserData
import BgTabManager
import joinTabManager
import joinDirManager
import PdfInfo
import PdfPageInfo
import rotate
import splitTabManager

from tkinter import filedialog
from pygubu import Builder as pgBuilder

# if dist fails to start because it's missing these, uncomment these two imports
# import pygubu.builder.ttkstdwidgets
# import pygubu.builder.widgets.dialog

from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter

# check to see if we're running from stand-alone one-file executable:
if hasattr(sys, '_MEIPASS'):
    CURRENT_DIR = sys._MEIPASS
else:
    CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
USER_DIR = str(plPath.home())
CONFIG_DIR = appdirs.user_config_dir(APPNAME)
DATA_DIR = appdirs.user_data_dir(APPNAME)


class PyPDFBuilderApplication:
    '''Main application class. Handles setup and running of all application parts.'''

    def __init__(self):
        self.builder = pgBuilder()
        self.builder.add_from_file(os.path.join(CURRENT_DIR, 'mainwindow.ui'))

        self.__mainwindow = self.builder.get_object('MainWindow')
        self.__notebook = self.builder.get_object('AppNotebook')
 		# ''' Add in the shortcut key binding '''
        self.__tabs = {
            'join': self.builder.get_object('JoinFrame'),
            'joinDir': self.builder.get_object('JoinDirFrame'),
            'split': self.builder.get_object('SplitFrame'),
            'bg': self.builder.get_object('BgFrame'),
            'rotate': self.builder.get_object('RotateFrame'),
        }
        self.__mainmenu = self.builder.get_object('MainMenu')
        self.__mainwindow.config(menu=self.__mainmenu)
        self.__status_text_variable = self.builder.get_variable('application_status_text')
        self.status_text = None
        self.builder.connect_callbacks(self)

        self.user_data = UserData()

        self.__jointab = JoinTabManager(self)
        self.__joinDtab = JoinDirManager(self)
        self.__splittab = SplitTabManager(self)
        self.__bgtab = BgTabManager(self)
        self.__rotatetab = RotateTabManager(self)


        self.status_text = DEFAULT_STATUS

    @property
    def status_text(self):
        return self.__status_text_variable.get()

    @status_text.setter
    def status_text(self, val):
        self.__status_text_variable.set(val)

    # Their has to be better way but for now this works
    def select_tab_join(self, *args, **kwargs):
    	''' Called when menu item "View" > "Join Files" '''
    	self.__notebook.select(self.__tabs['join'])

    def select_tab_split(self, *args, **kwargs):
    	''' Called when menu item "View" > "Split File" '''
    	self.__notebook.select(self.__tabs['split'])

    def select_tab_bg(self, *args, **kwargs):
    	''' Called when menu item "View" > "Background/Stamp/Number" '''
    	self.__notebook.select(self.__tabs['bg'])

    def select_tab_rotate(self, *args, **kwargs):
    	''' Called when menu item "View" > "Rotate Pages" '''
    	self.__notebook.select(self.__tabs['rotate'])

    def jointab_add_file(self):
        self.__jointab.add_file()

    def jointab_on_file_select(self, event):
        self.__jointab.on_file_select(event)

    def jointab_enter_page_selection(self, event):
        self.__jointab.enter_page_selection(event)

    def jointab_save_as(self):
        self.__jointab.save_as()

    def jointab_move_up(self):
        self.__jointab.move_up()

    def jointab_move_down(self):
        self.__jointab.move_down()

    def jointab_remove(self):
        self.__jointab.remove_file()




    def joinDtab_add_file(self):
        self.__joinDtab.add_file()

    def joinDtab_on_file_select(self, event):
        self.__joinDtab.on_file_select(event)

    def joinDtab_enter_page_selection(self, event):
        self.__joinDtab.enter_page_selection(event)

    def joinDtab_save_as(self):
        self.__joinDtab.save_as()

    def joinDtab_move_up(self):
        self.__joinDtab.move_up()

    def joinDtab_move_down(self):
        self.__joinDtab.move_down()

    def joinDtab_remove(self):
        self.__joinDtab.remove_file()






    def splittab_open_file(self):
        self.__splittab.open_file()

    def splittab_save_as(self):
        self.__splittab.save_as()

    def bgtab_choose_bg_option(self):
        self.__bgtab.choose_bg_option()

    def bgtab_choose_stamp_option(self):
        self.__bgtab.choose_stamp_option()

    def bgtab_choose_number_option(self):
    	''' Will ignore because it doesn't exist '''
    	pass

    def bgtab_choose_source_file(self):
        self.__bgtab.choose_source_file()

    def bgtab_choose_bg_file(self):
        self.__bgtab.choose_bg_file()

    def bgtab_save_as(self):
        self.__bgtab.save_as()

    def rotatetab_open_file(self):
        self.__rotatetab.open_file()

    def rotatetab_save_as(self):
        self.__rotatetab.save_as()

    def save_success(self, status_text=DEFAULT_STATUS):
        '''Gets called when a PDF file was processed successfully. Currently only
        increases the `number_of_processed_files`-counter by 1
        '''
        self.user_data.number_of_processed_files += 1
        self.status_text = status_text

    def show_settings(self, *args, **kwargs):
        ''' Throws a short error if delete but is unused'''
        self.__settings_dialog.run()

    def close_settings(self, *args, **kwargs):
        self.__settings_dialog.close()

    def cancel_settings(self, *args, **kwargs):
        pass

    def get_file_dialog(self, func, widget_title='Choose File(s) …'):
        f = func(
            initialdir=self.user_data.filedialog_path,
            title=widget_title,
            filetypes=(("PDF File", "*.pdf"), ("All Files", "*.*"))
        )
        if f:
            if type(f) == list or type(f) == tuple:
                self.user_data.filedialog_path = os.path.dirname(f[-1])
            elif type(f) == str:
                self.user_data.filedialog_path = os.path.dirname(f)
            return f

    def quit(self, event=None):
        self.__mainwindow.quit()

    def run(self):
        self.__mainwindow.mainloop()


if __name__ == '__main__':
    app = PyPDFBuilderApplication()
    app.run()
