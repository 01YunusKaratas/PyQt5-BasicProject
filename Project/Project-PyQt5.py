import sys
from PyQt5 import QtWidgets, QtGui, QtCore


class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.yazı_alanı = QtWidgets.QLineEdit()
        self.temizle = QtWidgets.QPushButton("Clear")
        self.yazdır = QtWidgets.QPushButton("Write")

        # Arka plan rengi ayarlama
        p = self.palette()
        p.setColor(self.backgroundRole(), QtGui.QColor(50, 50, 50))
        self.setPalette(p)

        #arka plan reim ekleme
        oImage = QtGui.QImage("python.png").scaled(self.size())
        sImage = oImage.scaled(QtCore.QSize(self.width(), self.height()))
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(sImage))
        self.setPalette(palette)





        # Düğme rengi ayarlama
        self.temizle.setStyleSheet("background-color: red; color: white;")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addStretch()
        v_box.addWidget(self.yazı_alanı)
        v_box.addWidget(self.yazdır)
        v_box.addWidget(self.temizle)
        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.temizle.clicked.connect(self.click)
        self.yazdır.clicked.connect(self.click)
        self.show()

    def click(self):
        sender = self.sender()
        if(sender.text() == "Clear"):
            if(self.yazı_alanı.text() == ""):
                return ""
            else:
                print("Line deleted")
                return self.yazı_alanı.clear()

        else:
            print(self.yazı_alanı.text())


app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
pencere.setGeometry(100, 100, 475,475)
sys.exit(app.exec())
