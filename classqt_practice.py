from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


from calculate import Ui_Dialog
import sys

class MyCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        #self.widge = QWidget() #combobox needed但包含在QMainWindow

        self.ui.addButton.clicked.connect(self.add)
        self.ui.pic.mousePressEvent = self.pic_clicked
        self.ui.comboBox.addItems(["English","中文"])
        self.ui.comboBox.activated.connect(self.change) 

        group1 = QButtonGroup(self) #QMainWindow包含widge 直接用self
        group1.addButton(self.ui.radioButton)
        group1.addButton(self.ui.radioButton_2)
        group1.addButton(self.ui.radioButton_3)
        group1.addButton(self.ui.radioButton_4)
        self.ui.radioButton.clicked.connect(self.add)
        self.ui.radioButton_2.clicked.connect(self.add)
        self.ui.radioButton_3.clicked.connect(self.add)
        self.ui.radioButton_4.clicked.connect(self.add)

    def is_float(self,num): #判斷是不是數字(整數/小數)
        try:
            float(num)
            return True
        except ValueError:
            return False
    
    def add(self):
        x = self.ui.numberone.text()
        y = self.ui.number_2.text()
        if self.ui.checkBox.isChecked():
            x=self.ui.number_2.text()
            y=self.ui.numberone.text()

        if not self.is_float(x) or not self.is_float(y): #判斷false先傳出去
            message = QMessageBox()
            message.setWindowTitle("wrong")
            message.setInformativeText("please enter number")
            message.exec_()
            return

        if self.ui.radioButton.isChecked():
            result = round(float(x)+float(y),2)
        elif self.ui.radioButton_2.isChecked():
            result = round(float(x)-float(y),2)
        elif self.ui.radioButton_3.isChecked():
            result = round(float(x)*float(y),2)
        elif self.ui.radioButton_4.isChecked():
            result = round(float(x)/float(y),2)      
        else:
            message = QMessageBox()
            message.setWindowTitle("wrong")
            message.setInformativeText("please choose")
            message.exec_()
            return 

        self.ui.label.setText(str(result)) 

    def pic_clicked(self,event):
        message = QMessageBox()
        message.setWindowTitle("surprise")
        message.setInformativeText("躺")
        message.exec_()

    def change(self):
        if self.ui.comboBox.currentIndex() ==0:
            self.ui.language.setText("Answer is...") 
        else:
            self.ui.language.setText("答案是...")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyCalculator()
    myWindow.show()
    sys.exit(app.exec_())
