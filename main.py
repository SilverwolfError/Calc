import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget

import CalcForPyQt01_MainWindow
import CalcForPyQt01_AdditionDialog

def showDialog():
    dialog = QDialog()
    ui = CalcForPyQt01_AdditionDialog.Ui_Dialog()
    ui.setupUi(dialog)
    dialog.exec_()

def close_window(self):
    MainWindow.close()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = CalcForPyQt01_MainWindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.AdditionButton.clicked.connect(showDialog)
    sys.exit(app.exec_())
