from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle('Twibuse')
    window.setGeometry(700, 400, 700, 400)

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()