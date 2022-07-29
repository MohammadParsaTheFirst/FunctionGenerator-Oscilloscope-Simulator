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

import Main
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QVBoxLayout
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from PyQt5 import QtCore, QtGui, QtWidgets

import gui


class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)
        self.figure = plt.figure()

        self.canvas = FigureCanvasQTAgg(self.figure)
        self.axis = self.figure.add_subplot(111)

        self.layoutvertical = QVBoxLayout(self)
        self.layoutvertical.addWidget(self.canvas)


class MainWidget(QWidget, gui.Ui_Dialog):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.setupUi(self)
        self.wavename = 'sine'
        self.frequencyValue = 1
        self.rising = True
        self.matplotwidget = MatplotlibWidget()
        self.layoutvertical = QVBoxLayout(self.widget)
        self.layoutvertical.addWidget(self.matplotwidget)

        self.dial.setValue(50)
        self.dial_2.setValue(50)
        self.dial_3.setValue(50)
        self.dial_4.setValue(20)
        self.dial_5.setValue(50)
        self.dial_6.setValue(50)
        self.dial_7.setValue(50)

        # self.plot_widget()
        self.anim1 = animation.FuncAnimation(self.matplotwidget.figure, self.update_sine, frames=2000, interval=10,
                                             blit=False)
        self.anim2 = animation.FuncAnimation(self.matplotwidget.figure, self.update_square, frames=2000, interval=10,
                                             blit=False)
        self.anim3 = animation.FuncAnimation(self.matplotwidget.figure, self.update_triangular, frames=2000,
                                             interval=10,
                                             blit=False)

        self.pushButton_sine.clicked.connect(self.changewave_to_sine)
        self.pushButton_square.clicked.connect(self.changewave_to_square)
        self.pushButton_tringular.clicked.connect(self.changewave_to_tri)

        self.pushButton_1.clicked.connect(self.changefrequency_to_1)
        self.pushButton_10.clicked.connect(self.changefrequency_to_10)
        self.pushButton_100.clicked.connect(self.changefrequency_to_100)
        self.pushButton_1k.clicked.connect(self.changefrequency_to_1k)
        self.pushButton_10k.clicked.connect(self.changefrequency_to_10k)
        self.pushButton_100k.clicked.connect(self.changefrequency_to_100k)

        self.radioButton.toggled.connect(self.set_rise)

        # self.dial.valueChanged.connect(self.plot_widget)
        # self.dial_3.valueChanged.connect(self.plot_widget)
        # self.dial_2.valueChanged.connect(self.plot_widget)
        self.dial_4.valueChanged.connect(self.plot)
        self.dial_5.valueChanged.connect(self.plot)
        self.trigger_level.valueChanged.connect(self.plot)
        # self.dial_6.valueChanged.connect(self.plot_widget)
        # self.dial_7.valueChanged.connect(self.plot_widget)

        self.plot()

    def plot(self):
        z = 0.000005 * np.exp(15 * self.dial_5.value() / 100)
        if self.wavename == 'sine':
            self.anim2.pause()
            self.anim3.pause()
            self.matplotwidget.axis.clear()
            self.matplotwidget.axis.set_facecolor("black")
            self.matplotwidget.axis.grid()
            self.x = np.linspace(-z, z, 1000)
            self.line, = self.matplotwidget.axis.plot([], [], 'yellow')
            self.anim1.resume()

        if self.wavename == 'square':
            self.anim1.pause()
            self.anim3.pause()
            self.matplotwidget.axis.clear()
            self.matplotwidget.axis.grid()
            self.matplotwidget.axis.set_facecolor("black")
            self.x = np.linspace(-z, z, 1000)
            self.line, = self.matplotwidget.axis.plot([], [], 'yellow')
            self.anim2.resume()

        if self.wavename == 'tri':
            self.anim1.pause()
            self.anim2.pause()
            self.matplotwidget.axis.clear()
            self.matplotwidget.axis.set_facecolor("black")
            self.matplotwidget.axis.grid()
            self.x = np.linspace(-z, z, 1000)
            self.line, = self.matplotwidget.axis.plot([], [], 'yellow')
            self.anim3.resume()

    def update_sine(self, i):
        z = 0.000005 * np.exp(15 * self.dial_5.value() / 100)
        if self.chech_trigger():
            self.matplotwidget.axis.set_ylim([-self.dial_4.value(), self.dial_4.value()])
            self.matplotwidget.axis.set_xlim([-z, z])
            self.matplotwidget.axis.axhline(y=50 - self.trigger_level.value())
            self.line.set_xdata(np.linspace(-z, z, 1000))
            self.line.set_ydata(
                self.dial_3.value() / 10 * np.sin(2 * np.pi * self.frequencyValue * (self.dial.value() / 100) * (
                        self.x - self.dial_7.value() / 10) + i / 10.0) - 50 + self.dial_2.value() - 50 + self.dial_6.value())  # update the data

        else:

            if self.rising:
                self.matplotwidget.axis.set_ylim([-self.dial_4.value(), self.dial_4.value()])
                self.matplotwidget.axis.set_xlim([-z, z])
                self.matplotwidget.axis.axhline(y=50 - self.trigger_level.value())
                self.line.set_xdata(np.linspace(-z, z, 1000))
                self.line.set_ydata(
                    self.dial_3.value() / 10 * np.sin(2 * np.pi * self.frequencyValue * (self.dial.value() / 100) * (
                            self.x - self.get_trigger_value_sine_rising() - self.dial_7.value() / 10)) - 50 + self.dial_2.value() - 50 + self.dial_6.value())  # update the data



            else:
                self.matplotwidget.axis.set_ylim([-self.dial_4.value(), self.dial_4.value()])
                self.matplotwidget.axis.set_xlim([-z, z])
                self.matplotwidget.axis.axhline(y=50 - self.trigger_level.value())
                self.line.set_xdata(np.linspace(-z, z, 1000))
                self.line.set_ydata(
                    self.dial_3.value() / 10 * np.sin(2 * np.pi * self.frequencyValue * (self.dial.value() / 100) * (
                            self.x + (1 / (2 * self.frequencyValue * (
                            self.dial.value() / 100))) - self.get_trigger_value_sine_falling() - self.dial_7.value() / 10)) - 50 + self.dial_2.value() - 50 + self.dial_6.value())  # update the data

        return self.line,

    def update_square(self, i):
        z = 0.000005 * np.exp(15 * self.dial_5.value() / 100)
        if self.chech_trigger():
            self.matplotwidget.axis.set_ylim([-self.dial_4.value(), self.dial_4.value()])
            self.matplotwidget.axis.set_xlim([-z, z])
            self.matplotwidget.axis.axhline(y=50 - self.trigger_level.value())
            self.line.set_xdata(np.linspace(-z, z, 1000))
            self.line.set_ydata(
                self.dial_3.value() / 10 * signal.square(2 * np.pi * self.frequencyValue * (self.dial.value() / 100) * (
                        self.x - self.dial_7.value() / 10) + i / 10.0,
                                                         0.5) - 50 + self.dial_2.value() - 50 + self.dial_6.value())  # update the data

        else:

            if self.rising == True:
                self.matplotwidget.axis.set_ylim([-self.dial_4.value(), self.dial_4.value()])
                self.matplotwidget.axis.set_xlim([-z, z])
                self.matplotwidget.axis.axhline(y=50 - self.trigger_level.value())
                self.line.set_xdata(np.linspace(-z, z, 1000))
                self.line.set_ydata(
                    self.dial_3.value() / 10 * signal.square(
                        2 * np.pi * self.frequencyValue * (self.dial.value() / 100) * (
                                self.x - 1 / (
                                2 * self.frequencyValue * (self.dial.value() / 100)) - self.dial_7.value() / 10),
                        0.5) - 50 + self.dial_2.value() - 50 + self.dial_6.value())  # update the data



            else:
                self.matplotwidget.axis.set_ylim([-self.dial_4.value(), self.dial_4.value()])
                self.matplotwidget.axis.set_xlim([-z, z])
                self.matplotwidget.axis.axhline(y=50 - self.trigger_level.value())
                self.line.set_xdata(np.linspace(-z, z, 1000))
                self.line.set_ydata(
                    self.dial_3.value() / 10 * signal.square(
                        2 * np.pi * self.frequencyValue * (self.dial.value() / 100) * (
                                self.x - self.dial_7.value() / 10)) - 50 + self.dial_2.value() - 50 + self.dial_6.value())  # update the data

        return self.line,

    def update_triangular(self, i):
        z = 0.000005 * np.exp(15 * self.dial_5.value() / 100)
        if self.chech_trigger():
            self.matplotwidget.axis.set_ylim([-self.dial_4.value(), self.dial_4.value()])
            self.matplotwidget.axis.set_xlim([-z, z])
            self.matplotwidget.axis.axhline(y=50 - self.trigger_level.value())
            self.line.set_xdata(np.linspace(-z, z, 1000))
            self.line.set_ydata(
                self.dial_3.value() / 10 * signal.sawtooth(
                    2 * np.pi * self.frequencyValue * (self.dial.value() / 100) * (
                            self.x - self.dial_7.value() / 10) + i / 10.0,
                    0.5) - 50 + self.dial_2.value() - 50 + self.dial_6.value())  # update the data

        else:

            if self.rising:
                self.matplotwidget.axis.set_ylim([-self.dial_4.value(), self.dial_4.value()])
                self.matplotwidget.axis.set_xlim([-z, z])
                self.matplotwidget.axis.axhline(y=50 - self.trigger_level.value())
                self.line.set_xdata(np.linspace(-z, z, 1000))
                self.line.set_ydata(
                    self.dial_3.value() / 10 * signal.sawtooth(
                        2 * np.pi * self.frequencyValue * (self.dial.value() / 100) * (
                                self.x - self.get_trigger_value_tri_rising() - self.dial_7.value() / 10),
                        0.5) - 50 + self.dial_2.value() - 50 + self.dial_6.value())  # update the data





            else:
                self.matplotwidget.axis.set_ylim([-self.dial_4.value(), self.dial_4.value()])
                self.matplotwidget.axis.set_xlim([-z, z])
                self.matplotwidget.axis.axhline(y=50 - self.trigger_level.value())
                self.line.set_xdata(np.linspace(-z, z, 1000))
                self.line.set_ydata(
                    self.dial_3.value() / 10 * signal.sawtooth(
                        2 * np.pi * self.frequencyValue * (self.dial.value() / 100) * (
                                self.x + (1 / (2 * self.frequencyValue * (
                                self.dial.value() / 100))) - self.get_trigger_value_tri_falling() - self.dial_7.value() / 10),
                        0.5) - 50 + self.dial_2.value() - 50 + self.dial_6.value())  # update the data


        return self.line,

    def Color_of_w(self):
        self.pushButton_sine.setStyleSheet("background-color : Gray;\n"
"border :3px solid black")
        self.pushButton_tringular.setStyleSheet("background-color : Gray;\n"
"border :3px solid black")
        self.pushButton_square.setStyleSheet("background-color : Gray;\n"
"border :3px solid black")

    def changewave_to_sine(self):
        self.Color_of_w()
        self.pushButton_sine.setStyleSheet("background-color : red;\n"
"border :3px solid black")
        self.wavename = 'sine'
        self.plot()

    def changewave_to_square(self):
        self.Color_of_w()
        self.pushButton_square.setStyleSheet("background-color : red;\n"
"border :3px solid black")
        self.wavename = 'square'
        self.plot()

    def changewave_to_tri(self):
        self.Color_of_w()
        self.pushButton_tringular.setStyleSheet("background-color : red;\n"
"border :3px solid black")
        self.wavename = 'tri'
        self.plot()

    def Color_of_f(self):
        self.pushButton_1.setStyleSheet("background-color : Gray;\n"
"border :3px solid black")
        self.pushButton_10.setStyleSheet("background-color : Gray;\n"
"border :3px solid black")
        self.pushButton_100.setStyleSheet("background-color : Gray;\n"
"border :3px solid black")
        self.pushButton_1k.setStyleSheet("background-color : Gray;\n"
"border :3px solid black")
        self.pushButton_10k.setStyleSheet("background-color : Gray;\n"
"border :3px solid black")
        self.pushButton_100k.setStyleSheet("background-color : Gray;\n"
"border :3px solid black")

    def changefrequency_to_1(self):
        self.Color_of_f()
        self.pushButton_1.setStyleSheet("background-color : red;\n"
"border :3px solid black")
        self.frequencyValue = 1
        self.plot()

    def changefrequency_to_10(self):
        self.Color_of_f()
        self.pushButton_10.setStyleSheet("background-color : red;\n"
"border :3px solid black")
        self.frequencyValue = 10
        self.plot()

    def changefrequency_to_100(self):
        self.Color_of_f()
        self.pushButton_100.setStyleSheet("background-color : red;\n"
"border :3px solid black")
        self.frequencyValue = 100
        self.plot()

    def changefrequency_to_1k(self):
        self.Color_of_f()
        self.pushButton_1k.setStyleSheet("background-color : red;\n"
"border :3px solid black")
        self.frequencyValue = 1000
        self.plot()

    def changefrequency_to_10k(self):
        self.Color_of_f()
        self.pushButton_10k.setStyleSheet("background-color : red;\n"
"border :3px solid black")
        self.frequencyValue = 10000
        self.plot()

    def changefrequency_to_100k(self):
        self.Color_of_f()
        self.pushButton_100k.setStyleSheet("background-color : red;\n"
"border :3px solid black")
        self.frequencyValue = 100000
        self.plot()

    def chech_trigger(self):
        if 50 - self.trigger_level.value() > self.dial_3.value() / 10 - 50 + self.dial_2.value() - 50 + self.dial_6.value() or 50 - self.trigger_level.value() < -self.dial_3.value() / 10 - 50 + self.dial_2.value() - 50 + self.dial_6.value():
            return True

        else:
            return False

    def get_trigger_value_sine_rising(self):
        ans = (100 / (2 * np.pi * self.frequencyValue * self.dial.value())) * np.arcsin((10 / self.dial_3.value()) * (
                50 - self.trigger_level.value() + 100 - self.dial_2.value() - self.dial_6.value())) + self.dial_7.value() / 10
        return -ans

    def get_trigger_value_sine_falling(self):
        ans = (100 / (2 * np.pi * self.frequencyValue * self.dial.value())) * np.arcsin((10 / self.dial_3.value()) * (
                 - 50 + self.trigger_level.value() + 100 - self.dial_2.value() - self.dial_6.value())) + self.dial_7.value() / 10
        return -ans

    def get_trigger_value_tri_falling(self):
        ans = (100 / (2 * np.pi * self.frequencyValue * self.dial.value())) * self.arc_triangular(
            (10 / self.dial_3.value()) * (
                    - 50 + self.trigger_level.value() + 100 - self.dial_2.value() - self.dial_6.value())) + self.dial_7.value() / 10
        return -ans

    def get_trigger_value_tri_rising(self):
        ans = (100 / (2 * np.pi * self.frequencyValue * self.dial.value())) * self.arc_triangular(
            (10 / self.dial_3.value()) * (
                     50 - self.trigger_level.value() + 100 - self.dial_2.value() - self.dial_6.value())) + self.dial_7.value() / 10
        return -ans

    def arc_triangular(self, x):
        return (np.pi / 2) * (x + 1)

    def set_rise(self):
        if self.radioButton.isChecked():
            self.rising = True
            self.plot()

        else:
            self.rising = False
            self.plot()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWidget()
    w.show()
    sys.exit(app.exec_())
