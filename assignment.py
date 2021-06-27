import sys,os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
def window():
   app = QApplication(sys.argv)
   w = QWidget()
   all_button = QPushButton(w)
   all_button.setText("ALL")
   all_button.move(1000,20)
   
   good_button = QPushButton(w)
   good_button.setText("GOOD")
   good_button.move(1100,20)
   
   bad_button = QPushButton(w)
   bad_button.setText("BAD")
   bad_button.move(1200,20)
   
   #w.setGeometry(100,100,200,50)
   
   scroll = QScrollArea(w)
   horizontalGroupBox = QGroupBox(scroll)
   
   layout = QGridLayout(horizontalGroupBox)
   
   #layout.setHorizontalSpacing(500)
   #layout.setVerticalSpacing(500)
   layout.setColumnStretch(1, 4)
   layout.setColumnStretch(2, 4)
   row=0
   column=0
     
   scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
   scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
   scroll.setWidgetResizable(True)

   

   for i in os.listdir("D:\\suman\\img\\"):
       label = QLabel(w)
       pixmap = QPixmap('D:\\suman\\img\\'+i)
       label.setPixmap(pixmap)
       pixmap = pixmap.scaled(100, 100)
       label.setPixmap(pixmap)
       
       layout.addWidget(label,row,column)
       column=column+1
       if column%10==0 :
            row=row+1
            column=0
       
        

   horizontalGroupBox.setContentsMargins(30, 20, 30, 30)       
       
       

   
   
   horizontalGroupBox.setLayout(layout)   
   scroll.setWidget(horizontalGroupBox)
   

   
   w.setWindowTitle("PyQt5")
   w.show()
   sys.exit(app.exec_())
if __name__ == '__main__':
   window()