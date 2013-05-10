# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui, uic
import sys

class MyWindow(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)
        uic.loadUi("Ui_Forms/Say_Hello.ui", self)   #Загружаем ui форму
                                                    #Теперь все компоненты формы доступны через self по их
                                                    # именам заданным в дизайнере в поле objectName
#        QtGui.QLabel("Add!",self)
        self.connect(self.btnQuit, QtCore.SIGNAL("clicked()"), QtGui.qApp, QtCore.SLOT('quit()'))
        self.connect(self.btnSaid, QtCore.SIGNAL("clicked()"), self.onSaid) #В качестве реакции на сигнал назначаем метод

    def onSaid(self):
        print(self.lineEdit.text())


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Подключение ui модуля")
    window.show()
    sys.exit(app.exec_())