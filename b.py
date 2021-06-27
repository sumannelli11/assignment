from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow,QGridLayout)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic
import sys,os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        #self.paintEvent()
 

    def initUI(self):
        self.scroll = QScrollArea()             # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()                 # Widget that contains the collection of Vertical Box
        painter = QPainter()
        self.vbox = QGridLayout()               # The Vertical Box that contains the Horizontal Boxes of  labels and buttons
        self.vbox.addWidget(QPushButton("Add"),0,7)
        self.vbox.addWidget(QPushButton("Good"),0,8)
        self.vbox.addWidget(QPushButton("Bad"),0,9)
        row=3
        column=0
        
        
        for i in os.listdir("D:\\suman\\img\\"):
           label = QLabel()
           
           
           pixmap = QPixmap('D:\\suman\\img\\'+i)
           
           
        
           pixmap = pixmap.scaled(100, 100)
         
           label.setPixmap(pixmap)

           self.vbox.addWidget(label,row,column)
           column=column+1
           if column%10==0 :
                row=row+1
                column=0

        self.widget.setLayout(self.vbox)

        #Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        self.setGeometry(600, 100, 1000, 900)
        self.setWindowTitle('Scroll Area Demonstration')
        self.show()

        return

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()