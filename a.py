from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow,QGridLayout)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic
import sys,os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from line import Example
from db_operations import db_op

class MainWindow(QMainWindow):

    
    
    def __init__(self):
        super().__init__()
        self.initUI()
        #self.paintEvent()
    def all_button_flag(self):
        global flag
        flag="all"
        if self.vbox is not None:
            while self.vbox.count():
                item = self.vbox.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.self.vbox)
            
            
            #self.vbox.itemAt(i).widget().setParent(None)
        self.initUI()
    def bad_button_flag(self):
        print("Bad is called"+str(self.vbox.count()))
        global flag
        flag="bad"
        if self.vbox is not None:
            while self.vbox.count():
                item = self.vbox.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.self.vbox)
            
            
            #self.vbox.itemAt(i).widget().setParent(None)
        self.initUI()
        
    def good_button_flag(self):
        global flag
        flag="good"
        if self.vbox is not None:
            while self.vbox.count():
                item = self.vbox.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.self.vbox)
            
            
            #self.vbox.itemAt(i).widget().setParent(None)
        self.initUI()

    def initUI(self):
        global flag
        print("the flag is "+flag)
        
        self.scroll = QScrollArea()             # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()                 # Widget that contains the collection of Vertical Box
        painter = QPainter()
        self.vbox = QGridLayout()               # The Vertical Box that contains the Horizontal Boxes of  labels and buttons
        all_button=QPushButton("All")
        self.vbox.addWidget(all_button,0,7)
        all_button.clicked.connect(self.all_button_flag)
        good_button=QPushButton("Good")
        good_button.clicked.connect(self.good_button_flag)
        self.vbox.addWidget(good_button,0,8)
        bad_button=QPushButton("Bad")
        bad_button.clicked.connect(self.bad_button_flag)
        self.vbox.addWidget(bad_button,0,9)
        db_fetch_all_default=db_op()
        if flag=="default" or flag=="all":
            data_all_default=db_fetch_all_default.all_data_fetch()
        elif flag=="good":
            data_all_default=db_fetch_all_default.good_data()
        else:
            data_all_default=db_fetch_all_default.bad_data()
        
        

        row=3
        column=0
        
        
        for i in data_all_default:
           label = QLabel()
           
           
           pixmap = QPixmap('D:\\suman\\img\\'+i["SKU Id"])
           a = Example("D:\\suman\\img\\"+str(i["SKU Id"]),i["Status"])
           #a.show()
           
        
           pixmap = pixmap.scaled(100, 100)
         
           label.setPixmap(pixmap)

           self.vbox.addWidget(a,row,column)
        
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
    global flag
    flag="default"
    main()