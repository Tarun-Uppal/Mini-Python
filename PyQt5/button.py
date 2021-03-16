import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox
from PyQt5 import QtWidgets

def dialog():
    mbox = QMessageBox()

    mbox.setText("Your allegiance has been noted")
    mbox.setDetailedText("You are now a disciple and subject of the all-knowing Guru")
    mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            
    mbox.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.showMaximized() 
    w.setWindowTitle('Temp')
    
    label = QLabel(w)
    label.setText("Test")
    label.move(100,130)
    label.show()

    btn = QPushButton(w)
    btn.setText('Beheld')
    btn.move(110,150)
    btn.show()
    btn.clicked.connect(dialog)

    
    w.show()
    sys.exit(app.exec_())