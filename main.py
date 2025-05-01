import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import CalcAlpha03ForPyQt

def click_addition():
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        ui = CalcAlpha03ForPyQt.Ui_Dialog()
        ui.setupUi(MainWindow)
        MainWindow.show()
        ui.AdditionButton.clicked.connect(click_addition)
        sys.exit(app.exec_())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = CalcAlpha03ForPyQt.Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.AdditionButton.clicked.connect(click_addition)
    sys.exit(app.exec_())