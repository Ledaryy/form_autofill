from PyQt5.QtCore import*
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CircularProgress(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        #CUSTOM PROPERTIES
        self.value = 0
        self.width = 200
        self.height = 200
        self.progress_width = 10
        self.progress_rounded_cap = True
        self.progress_color = 0x498BD1
        self.max_value = 100
        self.font_family = "Segoe UI"
        self.font_size = 12
        self.suffix = "%"
        self.text_color = 0x498BD1
        self.enable_shadow = True


        #Set default size without layout
        self.resize(self.width, self.height)

    #set value
    def set_value(self, value):
        self.value = value
        self.repaint() # render progress bar after

    #paint event (DESIGN YOUR CIRCULAR PROGRESS HERE)
    def paintEvent(self, event):
        #set progress parameters
        width = self.width - self.progress_width
        height = self.height - self.progress_width
        margin = self.progress_width / 2
        #margin = 5 #Test
        value = self.value * 360 / self.max_value

        #Painter
        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing) #remove pixelated edges
        paint.setFont(QFont(self.font_family, self.font_size))

        #Create rectangle
        rect = QRect(0, 0, self.width, self.height)
        paint.setPen(Qt.NoPen)
        paint.drawRect(rect)

        #PEN
        pen = QPen()
        pen.setColor(QColor(self.progress_color))
        pen.setWidth(self.progress_width)

        #Set Round Cap
        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.RoundCap)

        #Create arc / circular progress
        paint.setPen(pen)
        paint.drawArc(
            int(margin),
            int(margin), 
            width, 
            height, 
            -90 * 16, 
            int(-value) * 16
        )
       
       #create text
        pen.setColor(QColor(self.text_color))
        paint.setPen(pen)
        paint.drawText(rect, Qt.AlignCenter, f"{self.value}{self.suffix}")


        #END
        paint.end()