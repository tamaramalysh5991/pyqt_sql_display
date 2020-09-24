import sys
from PyQt5 import QtWidgets
import design


class DatabaseApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.executeButton.clicked.connect(self.execute_query)

    def execute_query(self):
        pass


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = DatabaseApp()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()

