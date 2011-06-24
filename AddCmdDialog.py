# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/sinan/dinleyici/AddCmdDialog.ui'
#
# Created: Tue Jun 21 11:59:45 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AddCmdDialog(object):
    def setupUi(self, AddCmdDialog):
        AddCmdDialog.setObjectName(_fromUtf8("AddCmdDialog"))
        AddCmdDialog.resize(400, 136)
        self.gridLayout = QtGui.QGridLayout(AddCmdDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(AddCmdDialog)
        self.label.setStyleSheet(_fromUtf8("color: white"))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.formatField = QtGui.QLineEdit(AddCmdDialog)
        self.formatField.setObjectName(_fromUtf8("formatField"))
        self.gridLayout.addWidget(self.formatField, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(AddCmdDialog)
        self.label_2.setStyleSheet(_fromUtf8("color: white"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.cmdField = QtGui.QLineEdit(AddCmdDialog)
        self.cmdField.setObjectName(_fromUtf8("cmdField"))
        self.gridLayout.addWidget(self.cmdField, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(AddCmdDialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monospace"))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color: white"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)
        self.buttonBox = QtGui.QDialogButtonBox(AddCmdDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 2)

        self.retranslateUi(AddCmdDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AddCmdDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AddCmdDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddCmdDialog)

    def retranslateUi(self, AddCmdDialog):
        AddCmdDialog.setWindowTitle(QtGui.QApplication.translate("AddCmdDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddCmdDialog", "Format", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddCmdDialog", "Command", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddCmdDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Monospace\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">_path_: Değiştirilen(oluşturulan) dosyanın yeri</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">_name_: Dosyanın adı(format dahil değil)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">_frm_ : Dosyanın formatı</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

