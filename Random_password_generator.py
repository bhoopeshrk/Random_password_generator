import random
# importing sys to pass bunch of arguments to QT and to initialize the QT application
import sys

# importing PyQt5 packages for GUI
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QFileDialog
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

# importing partial class from functools to pass arguments to the class while clicking the QpushButtons
from functools import partial

# importing os module for creating directries and files
import os

# importing ui python file
import UI.main as _main

# function for accessing files and folders created in temp folder
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
        
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

icons_directory = resource_path("icons/")

_logo = icons_directory + "password.ico"

class MainScreen(QDialog):
    def __init__(self):
        super(MainScreen, self).__init__()
        
        self.ui = _main.Ui_Dialog()
        self.ui.setupUi(self)
        
        self.setWindowIcon(QtGui.QIcon(_logo))
        self.setFixedSize(640,480)
        
        self.ui.passLabel.setText("")
        
        self.ui.Generate.clicked.connect(self.GeneratePass)
        
    def GeneratePass(self):
        plen = [i for i in range(6, 21)]        
        
        if self.ui.PassLen.text() == '':
            messageBox(title='Warning!', icon=QMessageBox.Warning, text = "Please enter password length")
            return
        else:
            try:
                length = int(self.ui.PassLen.text())
                
                if length not in plen:
                    messageBox(title='Warning!', icon=QMessageBox.Warning, text = "Please enter password length between 6 to 20")
                    return
                
                else:
                    string = 'abcdefghjiklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$&*()_-'
                    password = "".join(random.sample(string, length))
                    
                    self.ui.passLabel.setText(password)
                    
            except:
                messageBox(title='Warning!', icon=QMessageBox.Warning, text = "Please enter number")
                return
            
def messageBox(title = "Info", icon = QMessageBox.Warning, text = None):
    if text == None:
        return

    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setWindowIcon(QtGui.QIcon(_logo))
    msg.setIcon(icon)
    msg.setText(text)
    x = msg.exec_()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    
    main_screen = MainScreen()
    main_screen.show()

    try:
        sys.exit(app.exec_())
    
    except SystemExit:
        print('\nClosing application...')