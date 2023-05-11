#IMPORT MODULES
import sys
from PySide2 import QtCore, QtGui, QWidgets

#SPLASH SCREEN
class SplashScreen(QtWidgets.QMainWindow):
    def __init__(self):
        QWidgets.QMainWindow.__init__(self)
        self.ui=Ui_SplashScreen()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

if __name__=='__main__':
    app=QWidgets.QApplication([])
    window=SplashScreen()
    window.show()
    sys.exit(app.exec_())