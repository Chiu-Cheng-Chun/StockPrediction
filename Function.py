import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from UI import Ui_MainWindow #UI is not a package. It's our .py file

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        #inherit Ui_MainWindow
        super(MainWindow, self).__init__(parent)

        #Build UI
        self.setupUi(self)

        #"self.pushButton" funciton is in the UI.Ui_MainWindow
        #Cuz Ui_MainWindow is already inherited, implement self.pushButton
        # You have to check your button objectname
        self.pushButton.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText('Hi') #show the text

if __name__ == "__main__":
    app = QApplication(sys.argv) #call system
    window = MainWindow() #this class is instantiated
    window.show() #show the GUI
    sys.exit(app.exec_())#close system
