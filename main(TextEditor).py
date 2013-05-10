# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui, uic
import sys, os.path, datetime

def rel(*x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

class ConfirmExit(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        uic.loadUi("Ui_Forms/ConfirmExit.ui", self)
        self.setWindowFlags(QtCore.Qt.Window)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.parent = parent
        self.status = None

        self.connect(self.btnSave, QtCore.SIGNAL('clicked()'), self.save)
        self.connect(self.btnNo, QtCore.SIGNAL('clicked()'), self.no)
        self.connect(self.btnCancel, QtCore.SIGNAL('clicked()'), self.cancel)

    def save(self):
        self.status = "save"
        self.close()

    def no(self):
        self.status = "no"
        self.close()

    def cancel(self):
        self.status = "chancel"
        self.close()




class Path(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        uic.loadUi("Ui_Forms/Select_Path.ui", self)
        self.parent = parent
        self.path.setText(os.path.join(self.parent.dir, self.parent.file_name))

        self.connect(self, QtCore.SIGNAL('mySignal()'), QtCore.SLOT('close()') )
        self.connect(self.btnOK, QtCore.SIGNAL('clicked()'), self.saveToFile)


    def mousePressEvent(self, event):
        print('mousePressEvent')
        self.emit(QtCore.SIGNAL('mySignal()'))

    def saveToFile(self):
        print('save To file')
        text = self.parent.textEdit.toPlainText()
        path = self.path.text()
        try:
            fileHandle = open ( path, 'w' )
        except IOError:
            print('Директория, в которую пытаетесь сохранить файл, не существует!')
            return -1
        sep = path.rindex('\\')
        # print("dir = %s, file = %s"%(path[:sep],path[sep+1:]))
        self.parent.dir = path[:sep]
        self.parent.file_name = path[sep+1:]
        fileHandle.write(text)
        fileHandle.close()
        self.close()


class MyWindow(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)
        uic.loadUi("Ui_Forms/SaveLoad.ui", self)
        self.timer = QtCore.QTimer()

        self.connect(self.actionExit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
        self.connect(self.actionSave, QtCore.SIGNAL('triggered()'), self.save)
        self.connect(self.actionLoad, QtCore.SIGNAL('triggered()'), self.load)
        self.connect(self.textEdit, QtCore.SIGNAL('textChanged ()'), self.changeText)
        self.connect(self.timer, QtCore.SIGNAL("timeout()"), self.showTime)
        self.dir = rel('Docs')
        self.file_name = "data.txt"
        self.timer.start(1000)

    def saveToFile(self):
        print('save To file')
        text = self.textEdit.toPlainText()
        path =os.path.join(self.dir, self.file_name)
        try:
            fileHandle = open ( path, 'w' )
        except IOError:
            print('Директория, в которую пытаетесь сохранить файл, не существует!')
            return -1
        fileHandle.write(text)
        fileHandle.close()
        self.close()

    def changeText(self):
        # print(self.textEdit.toPlainText())
        self.l_numChars.setText(str(len(self.textEdit.toPlainText())))

    def showTime(self):
        self.l_time.setText(datetime.datetime.now().strftime("%H:%M:%S"))


    def save(self):
        print("save")
        self.child = Path(self)
        self.child.setWindowTitle('Select Path')
        self.child.setWindowFlags(QtCore.Qt.Window)
        self.child.setWindowModality(QtCore.Qt.WindowModal)
        self.child.show()


    def closeEvent(self, event):
        reply = ConfirmExit(self)
        reply.exec_()
        if reply.status == "save":
            self.saveToFile()
            event.accept()
        elif reply.status == "no":
            event.accept()
        else:
            event.ignore()


    def load(self):
        print("load")
        fileHandle = open ( os.path.join(self.dir, self.file_name), 'r' )
        text = fileHandle.read()
        self.textEdit.setText(text)
        fileHandle.close()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Mini TextEditor")
    # window.changeText()
    window.show()
    sys.exit(app.exec_())