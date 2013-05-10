# -*- coding: utf-8 -*-
# Обучающий пример. Создание окна с копоментами PyQT без Дезайнера форм.
from PyQt4 import QtCore, QtGui
import sys

#Класс для нашего окна, все окна в PyQT получаются наследование от базовых классов
class MyWindow(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent) #Вызываем конструктор родителя
        self.label = QtGui.QLabel("Привет, Мир!") #Создаем текстовую метку
        self.label.setAlignment(QtCore.Qt.AlignCenter) #Выравниваем метку по центру окна
        self.btnQuit = QtGui.QPushButton("&Окно закрывается") #Создаем кнопку с надписью "Окно закрывается"
        self.vbox = QtGui.QVBoxLayout() #Создаем вертикальный контейнер, для добавления в него копонентов
        self.vbox.addWidget(self.label) # Добавляем компонеты в контейнер
        self.vbox.addWidget(self.btnQuit)
        self.setLayout(self.vbox) #Добавляем контейнер в основное окно, контейнер становится потомком окна
        self.connect(self.btnQuit, QtCore.SIGNAL("clicked()"), QtGui.qApp.quit) #Назначаем обработчик сигнала

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv) #Создаем объект приложения
    window = MyWindow() #Создаем объект окна
    window.setWindowTitle("Тестовая программа на PyQt") #Задаем заголовок окна
    window.resize(300,70) #Изменяем размер окна
    window.show() #Делаем наше окно видимым
    sys.exit(app.exec_()) #Запускаем бесконечный цикл обработки сообщений приложения