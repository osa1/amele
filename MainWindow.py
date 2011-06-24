# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/sinan/dinleyici/MainWindow.ui'
#
# Created: Fri Jun 24 12:16:31 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName(_fromUtf8("MainForm"))
        MainForm.resize(683, 418)
        self.gridLayout_3 = QtGui.QGridLayout(MainForm)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tabWidget = QtGui.QTabWidget(MainForm)
        self.tabWidget.setMinimumSize(QtCore.QSize(500, 200))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.removeFolderButton = QtGui.QPushButton(self.tab)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/cross.png")), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.removeFolderButton.setIcon(icon)
        self.removeFolderButton.setObjectName(_fromUtf8("removeFolderButton"))
        self.gridLayout_2.addWidget(self.removeFolderButton, 1, 0, 1, 1)
        self.addFolderButton = QtGui.QPushButton(self.tab)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/tick.png")), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.addFolderButton.setIcon(icon1)
        self.addFolderButton.setObjectName(_fromUtf8("addFolderButton"))
        self.gridLayout_2.addWidget(self.addFolderButton, 1, 1, 1, 1)
        self.folderList = QtGui.QTreeWidget(self.tab)
        self.folderList.setRootIsDecorated(False)
        self.folderList.setItemsExpandable(False)
        self.folderList.setObjectName(_fromUtf8("folderList"))
        self.gridLayout_2.addWidget(self.folderList, 0, 0, 1, 2)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout = QtGui.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.commandTree = QtGui.QTreeWidget(self.tab_2)
        self.commandTree.setObjectName(_fromUtf8("commandTree"))
        self.gridLayout.addWidget(self.commandTree, 0, 0, 1, 2)
        self.removeCmdButton = QtGui.QPushButton(self.tab_2)
        self.removeCmdButton.setIcon(icon)
        self.removeCmdButton.setObjectName(_fromUtf8("removeCmdButton"))
        self.gridLayout.addWidget(self.removeCmdButton, 1, 0, 1, 1)
        self.addCmdButton = QtGui.QPushButton(self.tab_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/add.png")), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.addCmdButton.setIcon(icon2)
        self.addCmdButton.setObjectName(_fromUtf8("addCmdButton"))
        self.gridLayout.addWidget(self.addCmdButton, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.logTextEdit = QtGui.QTextEdit(self.tab_3)
        self.logTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.logTextEdit.setReadOnly(True)
        self.logTextEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.logTextEdit.setObjectName(_fromUtf8("logTextEdit"))
        self.gridLayout_4.addWidget(self.logTextEdit, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(MainForm)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(QtGui.QApplication.translate("MainForm", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.removeFolderButton.setText(QtGui.QApplication.translate("MainForm", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.addFolderButton.setText(QtGui.QApplication.translate("MainForm", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.folderList.headerItem().setText(0, QtGui.QApplication.translate("MainForm", "Recursive", None, QtGui.QApplication.UnicodeUTF8))
        self.folderList.headerItem().setText(1, QtGui.QApplication.translate("MainForm", "File Path", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainForm", "Folders", None, QtGui.QApplication.UnicodeUTF8))
        self.commandTree.headerItem().setText(0, QtGui.QApplication.translate("MainForm", "Format", None, QtGui.QApplication.UnicodeUTF8))
        self.removeCmdButton.setText(QtGui.QApplication.translate("MainForm", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.addCmdButton.setText(QtGui.QApplication.translate("MainForm", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainForm", "Commands", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("MainForm", "Log", None, QtGui.QApplication.UnicodeUTF8))

import data_rc
