import py_compile
from PyQt5.uic import compileUiDir, loadUi

ui_directory = "UI/"
if __name__ == "__main__":
    compileUiDir(ui_directory)