import sys
import time

import matplotlib.pyplot as plt
import matplotlib as plot
from PyQt5 import QtWidgets

from matplotlib import animation
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import numpy as np
from scipy import signal
import gui2
import Main3
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QVBoxLayout
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from PyQt5 import QtCore, QtGui, QtWidgets


class WelcomePage(QWidget, gui2.Ui_Dialog):
    def __init__(self):
        super(WelcomePage, self).__init__()
        self.setupUi(self)
        self.start_button.clicked.connect(self.change_window)

    def change_window(self):
        stackwidget.setCurrentIndex(stackwidget.currentIndex()+1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    stackwidget = QtWidgets.QStackedWidget()
    wp = WelcomePage()
    w = Main3.MainWidget()
    stackwidget.setWindowTitle("ECSP")
    stackwidget.addWidget(wp)
    stackwidget.addWidget(w)
    stackwidget.setFixedHeight(834)
    stackwidget.setFixedWidth(1118)
    stackwidget.setStyleSheet("background-color: rgb(54, 54, 54);")
    stackwidget.show()
    sys.exit(app.exec_())