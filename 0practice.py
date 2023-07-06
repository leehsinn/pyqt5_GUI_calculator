from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from calculate import Ui_Dialog
import sys

def is_float(num): #判斷是不是數字(整數/小數)
    try:
        float(num)
        return True
    except ValueError:
        return False
    
"""    if ui.radioButton.isChecked():
        result = round(float(x)+float(y),2)
    elif ui.radioButton_2.isChecked():
        result = round(float(x)-float(y),2)
    elif ui.radioButton_3.isChecked():
        result = round(float(x)*float(y),2)
    elif ui.radioButton_4.isChecked():
        result = round(float(x)/float(y),2)      
    else:
        message = QMessageBox()
        message.setWindowTitle("wrong")
        message.setInformativeText("please choose")
        message.exec_()
def calculate(x,y):
     """

def add():
    x = ui.numberone.text()
    y = ui.number_2.text()
    if ui.checkBox.isChecked():
        x=ui.number_2.text()
        y=ui.numberone.text()
        """tmp=x 交換寫法
        x=y
        y=tmp"""
    #check = x.isnumeric() 只能確認整數
    #check2 = y.isnumeric()
    if not is_float(x) or not is_float(y): #判斷false先傳出去
        message = QMessageBox()
        message.setWindowTitle("wrong")
        message.setInformativeText("please enter number")
        message.exec_()
        return

    if ui.radioButton.isChecked():
        result = round(float(x)+float(y),2)
    elif ui.radioButton_2.isChecked():
        result = round(float(x)-float(y),2)
    elif ui.radioButton_3.isChecked():
        result = round(float(x)*float(y),2)
    elif ui.radioButton_4.isChecked():
        result = round(float(x)/float(y),2)      
    else:
        message = QMessageBox()
        message.setWindowTitle("wrong")
        message.setInformativeText("please choose")
        message.exec_()
        return #避免整個視窗跳掉
    

    g = slider_change()
    final = g*0.01*result

    ui.label.setText(str(final)) 
    #result = x+y
    #ui.label.setText(str(result)) 


def pic_clicked(event):
    message = QMessageBox()
    message.setWindowTitle("surprise")
    message.setInformativeText("躺")
    message.exec_()

def change():
    if ui.comboBox.currentIndex() ==0:
        ui.language.setText("Answer is...") 
    else:
        ui.language.setText("答案是...") 

def slider_change():
    s = 1
    s = ui.horizontalSlider.value()
    ui.progressBar.setValue(s)
    return s

"""def slider_release():
    message = QMessageBox()
    message.setWindowTitle("surprise")
    message.setInformativeText("數值是"+str(ui.horizontalSlider.value()))
    message.exec_()   """

app = QApplication(sys.argv)
widge = QWidget()
ui = Ui_Dialog()
ui.setupUi(widge)
 
ui.progressBar.setMaximum(100)
ui.progressBar.setMinimum(0)
ui.progressBar.setValue(1)
ui.horizontalSlider.setMaximum(100)
ui.horizontalSlider.setMinimum(0)
ui.horizontalSlider.setValue(1)
ui.horizontalSlider.valueChanged.connect(slider_change)
#ui.horizontalSlider.sliderReleased.connect(slider_release)

ui.addButton.clicked.connect(add)
#ui.addButton.clicked.connect(change)

ui.pic.mousePressEvent = pic_clicked
ui.comboBox.addItems(["English","中文"])
ui.comboBox.activated.connect(change) 

group1 = QButtonGroup(widge) #radiobutton互斥(同時間只能選一個)
group1.addButton(ui.radioButton)
group1.addButton(ui.radioButton_2)
group1.addButton(ui.radioButton_3)
group1.addButton(ui.radioButton_4)
ui.radioButton.clicked.connect(add)
ui.radioButton_2.clicked.connect(add)
ui.radioButton_3.clicked.connect(add)
ui.radioButton_4.clicked.connect(add)


widge.show()
sys.exit(app.exec_())