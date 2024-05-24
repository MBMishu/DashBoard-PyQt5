import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt
from ui_interface import *

from PySide2.QtGui import QPainter
from PySide2.QtCharts import QtCharts

from functools import partial
import csv

from Custom_Widgets.Widgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.setMinimumSize(600, 600)
        loadJsonStyle(self, self.ui)
        self.show()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
