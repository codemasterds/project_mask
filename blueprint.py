# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(100, 100, 600, 400)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for widgets
    def UiComponents(self):
        # ______DropDown_______
        # creating a combo box widget
        combo_box = QComboBox(self)

        # setting geometry of combo box
        combo_box.setGeometry(50, 30, 120, 30)

        # geek list
        geek_list = ["America", "India", "Srilanka", "Austraila"]

        # adding list of items to combo box
        combo_box.addItems(geek_list)

        ## ______PushButton_____#

        button = QPushButton("CLICK", self)

        # setting geometry of button
        button.setGeometry(300, 30, 100, 30)

        # adding action to a button
        #button.clicked.connect(self.clickme)


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
