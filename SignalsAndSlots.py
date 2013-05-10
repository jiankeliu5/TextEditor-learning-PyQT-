#!/usr/bin/python
#Принципы работы с сигналами и слотами
# Слот — это метод, который реагирует на сигнал.
#Ссылка на источник: http://habrahabr.ru/post/31690/

import sys
from PyQt4 import QtGui, QtCore

class SigSlot(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setWindowTitle('signal & slot')

        lcd = QtGui.QLCDNumber(self)
        slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(slider)

        self.setLayout(vbox)
        self.connect(slider, QtCore.SIGNAL('valueChanged(int)'),#slider отсылает сигнал
            lcd, QtCore.SLOT('display(int)') )#lcd на него реагирует

        self.resize(250, 150)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()
        else:
            print(event.key())

app = QtGui.QApplication(sys.argv)
qb = SigSlot()
qb.show()
sys.exit(app.exec_())