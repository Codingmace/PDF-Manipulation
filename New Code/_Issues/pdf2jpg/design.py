# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pdf2jpg.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(621, 279)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sourceGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.sourceGroupBox.setGeometry(QtCore.QRect(10, 10, 600, 80))
        self.sourceGroupBox.setObjectName("sourceGroupBox")
        self.sourceFilePathLineEdit = QtWidgets.QLineEdit(self.sourceGroupBox)
        self.sourceFilePathLineEdit.setGeometry(QtCore.QRect(20, 30, 450, 34))
        self.sourceFilePathLineEdit.setObjectName("sourceFilePathLineEdit")
        self.sourceFileChooseButton = QtWidgets.QPushButton(self.sourceGroupBox)
        self.sourceFileChooseButton.setGeometry(QtCore.QRect(480, 30, 100, 36))
        self.sourceFileChooseButton.setObjectName("sourceFileChooseButton")
        self.destinationGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.destinationGroupBox.setGeometry(QtCore.QRect(10, 100, 600, 121))
        self.destinationGroupBox.setObjectName("destinationGroupBox")
        self.destinationFolderPathLineEdit = QtWidgets.QLineEdit(self.destinationGroupBox)
        self.destinationFolderPathLineEdit.setGeometry(QtCore.QRect(20, 30, 450, 34))
        self.destinationFolderPathLineEdit.setObjectName("destinationFolderPathLineEdit")
        self.destinationFolderChooseButton = QtWidgets.QPushButton(self.destinationGroupBox)
        self.destinationFolderChooseButton.setGeometry(QtCore.QRect(480, 30, 100, 36))
        self.destinationFolderChooseButton.setObjectName("destinationFolderChooseButton")
        self.dpiLabel = QtWidgets.QLabel(self.destinationGroupBox)
        self.dpiLabel.setGeometry(QtCore.QRect(20, 80, 63, 20))
        self.dpiLabel.setObjectName("dpiLabel")
        self.dpiComboBox = QtWidgets.QComboBox(self.destinationGroupBox)
        self.dpiComboBox.setGeometry(QtCore.QRect(100, 70, 83, 34))
        self.dpiComboBox.setFrame(True)
        self.dpiComboBox.setObjectName("dpiComboBox")
        self.dpiComboBox.addItem("")
        self.dpiComboBox.addItem("")
        self.dpiComboBox.addItem("")
        self.dpiComboBox.addItem("")
        self.convertButton = QtWidgets.QPushButton(self.centralwidget)
        self.convertButton.setGeometry(QtCore.QRect(210, 230, 94, 36))
        self.convertButton.setObjectName("convertButton")
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setGeometry(QtCore.QRect(310, 230, 94, 36))
        self.quitButton.setObjectName("quitButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "pdf2jpg"))
        self.sourceGroupBox.setTitle(_translate("MainWindow", "Source"))
        self.sourceFileChooseButton.setText(_translate("MainWindow", "Browse..."))
        self.destinationGroupBox.setTitle(_translate("MainWindow", "Destination"))
        self.destinationFolderChooseButton.setText(_translate("MainWindow", "Browse..."))
        self.dpiLabel.setText(_translate("MainWindow", "DPI"))
        self.dpiComboBox.setItemText(0, _translate("MainWindow", "72"))
        self.dpiComboBox.setItemText(1, _translate("MainWindow", "144"))
        self.dpiComboBox.setItemText(2, _translate("MainWindow", "300"))
        self.dpiComboBox.setItemText(3, _translate("MainWindow", "600"))
        self.convertButton.setText(_translate("MainWindow", "Convert"))
        self.quitButton.setText(_translate("MainWindow", "Quit"))
