import sys
import random
from PySide6.QtWidgets import QApplication, QWidget

import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("to-do list")
window.show()

app.exec()



