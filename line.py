import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Example(QWidget):
    def __init__(self,img_path,img_status):
        self.img_path=img_path
        self.img_status=img_status
        super().__init__()
        
        self.setGeometry(30, 30, 500, 300)
        
        
    

    def paintEvent(self,event):
        painter = QPainter(self)
        pixmap = QPixmap(self.img_path)
        pixmap = pixmap.scaled(100, 100)
        painter.drawPixmap(self.rect(),pixmap)
        if self.img_status=="good":
            pen = QPen(Qt.green, 10)
        else:
            pen = QPen(Qt.red, 10)
        
        painter.setPen(pen)
        
        painter.drawLine(10,self.rect().height() -2, self.rect().width() -10 , self.rect().height() -2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())