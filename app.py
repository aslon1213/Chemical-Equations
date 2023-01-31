import sys
from PyQt6 import QtWidgets, QtGui, QtCore

def main_window():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setWindowTitle("Chemical Reactions Simulator")
    window.setGeometry(300, 500, 1000, 800)
    window.move(60, 15)
    label = QtWidgets.QLabel(window)
    label.setText("My first label")
    label.move(60, 15)

    
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main_window()
