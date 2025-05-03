import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

import CalcForPyQt01_MainWindow
import CalcForPyQt01_AdditionDialog
import CalcForPyQt01_ResultShow

def showDialog(opr):
    global dialoginput
    global result
    dialoginput = QDialog()
    ui = CalcForPyQt01_AdditionDialog.Ui_Dialog()
    ui.setupUi(dialoginput)
    ui.Adder1PT.setReadOnly(True)
    ui.Adder2PT.setReadOnly(True)
    if opr == 'subtraction':
        ui.Adder1PT.setPlainText('subtrahend')
        ui.Adder2PT.setPlainText('minuends')
    elif opr == 'multiplication':
        ui.Adder1PT.setPlainText('multiplier')
        ui.Adder2PT.setPlainText('multiplicand')
    def calculation():
        try:
            global result
            if opr == 'add':
                result = str(int(ui.Adder1LE.text())+int(ui.Adder2LE.text()))
            elif opr == 'subtraction':
                result = str(int(ui.Adder1LE.text())-int(ui.Adder2LE.text()))
            elif opr == 'multiplication':
                result = str(int(ui.Adder1LE.text())*int(ui.Adder2LE.text()))
            showResult()
        except:
            result = 'Invalid Input'
            showResult()
    ui.GetResultButton.clicked.connect(calculation)
    dialoginput.exec_()

def showResult():
    global dialogoutput
    dialogoutput = QDialog()
    ui = CalcForPyQt01_ResultShow.Ui_Dialog()
    ui.setupUi(dialogoutput)
    ui.ShowResult.setReadOnly(True)
    ui.ShowResult.setPlainText(result)
    ui.OKButton.clicked.connect(lambda:close_all_windows(0))
    ui.CancelButton.clicked.connect(lambda:close_all_windows(1))
    dialogoutput.exec_()

def close_all_windows(pm):
    if pm == 0:
        dialoginput.close()
        dialogoutput.close()
    else:
        MainWindow.close()
        dialoginput.close()
        dialogoutput.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = CalcForPyQt01_MainWindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.AdditionButton.clicked.connect(lambda:showDialog('add'))
    ui.SubtractionButton.clicked.connect(lambda:showDialog('subtraction'))
    ui.MultiplicationButton.clicked.connect(lambda:showDialog('multiplication'))
    sys.exit(app.exec_())
