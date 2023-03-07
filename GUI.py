import sys
from PyQt5.QtWidgets import *

# app = QApplication(sys.argv)
# win = QWidget()
#
# win.setWindowTitle("Imperium")
# win.resize(1000, 900)
#
#
# win.show()
#
# app.exec_()
# sys.exit(app.exec_())

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.setWindowTitle("Imperium")

        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        file_menu2 = menubar.addMenu("Edit")
        file_menu3 = menubar.addMenu("View")

        new_action = QAction("New Window", self)
        file_menu.addAction(new_action)

        new_action = QAction("Close Window", self)
        file_menu.addAction(new_action)

        new_action.setStatusTip("New File")

        self.resize(500,500)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())

