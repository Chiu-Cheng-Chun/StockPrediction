import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPalette, QPixmap, QBrush
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication
from UI import Ui_MainWindow #UI is not a package. It's our .py file

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent) #inherit Ui_MainWindow
        self.setupUi(self) #Build UI

        #"self.pushButton" funciton is in the UI.Ui_MainWindow
        #Cuz Ui_MainWindow is already inherited, implement self.pushButton
        # You have to check your button objectname
        self.pushButton.clicked.connect(self.clicked)

        self.lineEdit.setText('Hi') #put text in lineEdit when start
        self.pushButton_2.clicked.connect(self.button2Clicked) # You have to check your button objectname
        self.setWindowTitle('This is our test!!') # MainWindow Title
        self.setWindowIcon(QtGui.QIcon('C://Users//craig//PycharmProjects//Stock_Predict//venv//picture//icon.png')) # Set Window Icon

        image = QPixmap() # Pixmap
        image.load('C://Users//craig//PycharmProjects//Stock_Predict//venv//picture//superpan.png') #load image
        image = image.scaled(self.width(), self.height()) #scale the image

        palette = QPalette() # Palette
        palette.setBrush(self.backgroundRole(), QtGui.QColor(200,200,100))#bg img setting
        self.setPalette(palette) #Apply the setting

    def clicked(self):
        self.label.setFont(QtGui.QFont('Arial', 50)) #set Font size
        self.label.setGeometry(QtCore.QRect(250, 300, 280, 150)) #QRect(int x, int y, int width, int height)

        pe = QPalette() # Palette
        pe.setColor(QPalette.WindowText, Qt.red) #set font color
        self.label.setAutoFillBackground(True)  #fill background. It's necessary before setting text-bg color
        pe.setColor(QPalette.Background,Qt.green) #set bg color
        self.label.setPalette(pe)  # Apply color setting

        self.label.setText('Im here!!') #show the text

    def button2Clicked(self): #for button_2 Clicked
        text = self.lineEdit.text() #get user input from lineEdit
        self.label_2.setText(text) #Show text on label_2
        self.lineEdit.clear() #clear user input

if __name__ == "__main__":
    app = QApplication(sys.argv) #call system
    window = MainWindow() #this class is instantiated
    window.show() #show the GUI
    sys.exit(app.exec_())#close system

