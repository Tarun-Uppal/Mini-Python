
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QFileDialog
from PyQt5 import QtWidgets

def dialog():
    filename = QFileDialog.getOpenFileName()
    print(filename[0])

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
    
