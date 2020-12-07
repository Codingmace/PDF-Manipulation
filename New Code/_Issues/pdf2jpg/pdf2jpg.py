#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import platform
import subprocess
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import design


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def choose_pdf(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self,
                                                   "Choose PDF file", "", "PDF files (*.pdf)",
                                                   options=options)
        self.sourceFilePathLineEdit.setText(file_name)

    def choose_destination_folder(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        options |= QFileDialog.ShowDirsOnly
        dir_name = QFileDialog.getExistingDirectory(self,
                                                    "Choose destination directory for images",
                                                    "/tmp",
                                                    options=options)
        self.destinationFolderPathLineEdit.setText(dir_name)

    def open_directory(self, directory_path):
        if platform.system() == "Windows":
            subprocess.check_call(["explorer", "/select", directory_path])
        elif platform.system() == "Darwin":
            subprocess.check_call(["open", "--", directory_path])
        else:
            subprocess.check_call(["xdg-open", directory_path])

    def convert(self):
        code = os.system(
            f"gs -dNOPAUSE -sDEVICE=jpeg -sOutputFile={self.destinationFolderPathLineEdit.text()}/page%03d.jpg -dJPEGQ=90 -r{self.dpiComboBox.currentText()} -q {self.sourceFilePathLineEdit.text()} -c quit")
        if code == 0:
            QMessageBox.information(self, self.window().windowTitle(), 'Done!', QMessageBox.Ok)
            self.open_directory(self.destinationFolderPathLineEdit.text())
        else:
            QMessageBox.critical(self, self.window().windowTitle(), 'Error!', QMessageBox.Ok)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Bind events
        self.sourceFileChooseButton.clicked.connect(self.choose_pdf)
        self.destinationFolderChooseButton.clicked.connect(self.choose_destination_folder)
        self.convertButton.clicked.connect(self.convert)
        self.quitButton.clicked.connect(self.close)

        self.dpiComboBox.setCurrentText('300')


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
