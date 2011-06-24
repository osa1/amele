#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import atexit

import monitor

from PyQt4 import QtGui
from PyQt4 import QtCore

from MainWindow import Ui_MainForm
from AddCmdDialog import Ui_AddCmdDialog

from notifier_backend import PAbstractBox
from notifier_backend import OUT, TOPCENTER, MIDCENTER, CURRENT, OUT, BOTCENTER
from notifier_backend import QProgressIndicator


class Main(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        centralWidget = QtGui.QWidget(self)
        self.ui = Ui_MainForm()
        self.ui.setupUi(centralWidget)
        self.setCentralWidget(centralWidget)

        self.__init_folder_list()
        self.__init_tray_icon()
        self.__init_shortcuts()
        self.__init_commands()

        self.ui.folderList.itemDoubleClicked.connect(self.toggle_subfolders)
        self.ui.addFolderButton.clicked.connect(self.__add_folder)
        self.ui.addCmdButton.clicked.connect(self.__add_cmd)
        self.ui.commandTree.doubleClicked.connect(self.__update_cmd)
        self.ui.removeCmdButton.clicked.connect(self.remove_selected_cmd)
        self.ui.removeFolderButton.clicked.connect(self.remove_selected_folder)

        self.cmdDialog = CmdDialog(self)
        self.cmdDialog.enableOverlay()
        self.cmdDialog.adjustSize()

    def __update_cmd(self, *args):
        item = self.ui.commandTree.currentItem()
        parent = item.parent()
        if parent:
            self.cmdDialog._form.formatField.setText(parent.text(0))
            self.cmdDialog._form.cmdField.setText(item.text(0))
            self.cmdDialog.showBox(self.update_cmd)

    def update_cmd(self, format, cmd):
        item = self.ui.commandTree.currentItem()
        old_format = item.parent().text(0)
        old_cmd = item.text(0)
        if format == old_format and cmd != old_cmd:
            monitor.remove_command(str(format), str(old_cmd))
            monitor.add_command(str(format), str(cmd))
        elif format != old_format and cmd == old_cmd:
            monitor.remove_command(str(old_format), str(cmd))
            monitor.add_command(str(format), str(cmd))
        elif format != old_format and cmd != old_cmd:
            monitor.remove_command(str(old_format), str(old_cmd))
            monitor.add_command(str(format), str(cmd))
        self.__init_commands()
        print monitor.commands

    def __init_shortcuts(self):
        shortcut = QtGui.QShortcut(QtGui.QKeySequence("ESC"), self)
        shortcut.activated.connect(self.minimize)
        shortcut = QtGui.QShortcut(QtGui.QKeySequence("CTRL+PgDown"), self)
        shortcut.activated.connect(self.prev_tab)
        shortcut = QtGui.QShortcut(QtGui.QKeySequence("CTRL+PgUp"), self)
        shortcut.activated.connect(self.next_tab)

    def __init_folder_list(self):
        self.ui.folderList.clear()
        folder_list = monitor.folders
        for folder in folder_list:
            item = QtGui.QTreeWidgetItem(self.ui.folderList)
            item.setText(0, str(folder[1]))
            item.setText(1, folder[0])

    def __init_commands(self):
        self.ui.commandTree.clear()
        qt = QtCore.Qt
        #flags = qt.ItemIsSelectable|qt.ItemIsEditable|qt.ItemIsDragEnabled| \
                #qt.ItemIsDropEnabled|qt.ItemIsUserCheckable|qt.ItemIsEnabled
        flags = qt.ItemIsSelectable | qt.ItemIsUserCheckable | qt.ItemIsEnabled
        commands = monitor.commands
        for frm in commands.keys():
            item = QtGui.QTreeWidgetItem(self.ui.commandTree, (frm,))
            item.setFlags(flags)
            for cmd in commands[frm]:
                subitem = QtGui.QTreeWidgetItem(item, (cmd,))
                subitem.setFlags(flags)

    def __init_tray_icon(self):
        icon = QtGui.QIcon(":/images/tick.png")
        self.__tray_icon = SystemTrayIcon(icon, self)
        self.__tray_icon.show()
        self.__tray_icon.activated.connect(self.activate)

    def __add_folder(self, folder):
        if not folder:
            folder = self.get_folder()
        if not folder:  # ehehe bu ne lan
            return
        monitor.add_folder(str(folder))  # cast QString to Python string
        self.__init_folder_list()
        # TODO her degisiklikte yenilemek yerine en son yenileme?
        monitor.reset_monitor()

    def __add_cmd(self):
        self.cmdDialog.showBox(self.add_cmd)

    def remove_selected_cmd(self, *args):
        item = self.ui.commandTree.currentItem()
        parent = item.parent()
        if parent:
            # cast QStrings to Python strings
            monitor.remove_command(str(parent.text(0)), str(item.text(0)))
        else:
            monitor.remove_command(str(item.text(0)))
        self.__init_commands()

    def remove_selected_folder(self, *args):
        item = self.ui.folderList.currentItem()
        monitor.remove_folder(str(item.text(1)))
        self.__init_folder_list()

    def add_cmd(self, format, cmd):
        monitor.add_command(format, cmd)
        self.__init_commands()

    def append_log(self, string):
        self.ui.logTextEdit.append(string)

    def get_folder(self):
        filename = QtGui.QFileDialog.getExistingDirectory(
                self, "Select target directory", "~/",
                QtGui.QFileDialog.ShowDirsOnly | QtGui.QFileDialog.DontResolveSymlinks)
        return filename

    def prev_tab(self):
        self.ui.tabWidget.setCurrentIndex((self.ui.tabWidget.currentIndex() + 1) %
                self.ui.tabWidget.count())

    def next_tab(self):
        self.ui.tabWidget.setCurrentIndex((self.ui.tabWidget.currentIndex() - 1) %
                self.ui.tabWidget.count())

    def hideEvent(self, evt):
        self.minimize()

    def toggle_subfolders(self):
        item = self.ui.folderList.selectedItems()[0]
        b = item.text(0)
        item.setText(0, "False" if b == "True" else "True")
        monitor.toggle_folder_recursion(self.ui.folderList.selectedItems()[0].text(1))
        monitor.reset_monitor()

    def minimize(self):
        self.hide()

    def activate(self):
        self.show()
        # minimize edildikten sonra tekrar gozukmesi icin gerekli
        # diger turlu, aciliyor ama arkaplanda kaliyor
        self.showNormal()

    def closeEvent(self, event):
        monitor.save_folders()
        monitor.save_commands()
        #reply = QtGui.QMessageBox.question(self, 'Message',
            #"Are you sure to quit?", QtGui.QMessageBox.Yes |
            #QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        #if reply == QtGui.QMessageBox.Yes:
            #event.accept()
        #else:
            #event.ignore()


class OutLog:  # TODO renkli yazdirma calismiyor
    def __init__(self, edit, out=None, color=None):
        """(edit, out=None, color=None) -> can write stdout, stderr to a
        QTextEdit.
        edit  = QTextEdit
        out   = alternate stream (can be the original sys.stdout )
        color = alternate color (i.e. color stderr a different color)
        """
        self.edit = edit
        self.out = None
        self.color = color

    def write(self, m):
        if self.color:
            tc = self.edit.textColor()
            self.edit.setTextColor(self.color)

        self.edit.moveCursor(QtGui.QTextCursor.End)
        self.edit.insertPlainText(m)

        if self.color:
            self.edit.setTextColor(tc)

        if self.out:
            self.out.write(m)


class SystemTrayIcon(QtGui.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        QtGui.QSystemTrayIcon.__init__(self, icon, parent)
        self.menu = QtGui.QMenu(parent)
        exitAction = self.menu.addAction("Exit")
        self.setContextMenu(self.menu)


class CmdDialog(PAbstractBox):
    def __init__(self, parent):
        PAbstractBox.__init__(self, parent)

        self._form = Ui_AddCmdDialog()
        self._form.setupUi(self)

        self._animation = 2
        self._duration = 500

        self._shown = False

    def showBox(self, accept=None, reject=None):
        """Call accept/reject methods when dialog accepted/rejected.
        accept method must have 2 arguments, one for format field
        and one for command field."""
        self._shown = True
        self.animate(start=MIDCENTER, stop=MIDCENTER)
        self.accept = accept
        self.reject = reject

    def hideBox(self):
        if self._shown:
            self.animate(start=MIDCENTER, stop=BOTCENTER, direction=OUT)

    def accept(self):
        self.hideBox()
        format = self._form.formatField.text()
        cmd = self._form.cmdField.text()
        self._form.formatField.setText("")
        self._form.cmdField.setText("")
        if self.accept:
            self.accept(format, cmd)

    def reject(self):
        self.hideBox()
        self._form.formatField.setText("")
        self._form.cmdField.setText("")
        if self.reject:
            self.reject()


# test--------------------------------
def main():
    monitor.load_commands()
    monitor.load_folders()

    app = QtGui.QApplication(sys.argv)
    test = Main()
    test.show()

    sys.stdout = OutLog(test.ui.logTextEdit, sys.stdout)
    sys.stderr = OutLog(test.ui.logTextEdit, sys.stderr, QtGui.QColor(255, 100, 200))

    monitor.start_monitor()

    app.exec_()
# test son ---------------------------

if __name__ == '__main__':
    main()
