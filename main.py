from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def main():
    app = QApplication(sys.argv)
    wind = QMainWindow()
    wind.setGeometry(900,300,300,300)
    wind.setWindowTitle("Estimation Auxiliary")

    wind.show()
    sys.exit(app.exec_())

main()