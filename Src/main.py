import os
import sys
import pyttsx3
import PyPDF2
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import *




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.left = 240
        self.top = 100
        self.height = 400
        self.widht = 400
        # =============================================
        self.setGeometry(self.left, self.top, self.widht, self.height)
        self.setWindowIcon(QIcon("Python_PyQt5.png"))  # Windows Icon
        self.setWindowTitle("AudioBook V02")
        self.player_widget = Window()
        self.setCentralWidget(self.player_widget)
        self.show()
        self.creatMenu()

    def creatMenu(self):
        # Creat Menu
        bar = self.menuBar()
        fileMenu = bar.addMenu("File")
        helpMenu = bar.addMenu("Help")

        # Create Actions

        opneFile = QAction(QIcon("open_file.png"), "Open PDF", self)
        opneFile.setShortcut("Ctrl+N")
        opneFile.triggered.connect(self.player_widget.open_file)
        fileMenu.addAction(opneFile)

        closeApplication = QAction(QIcon("exit.png"), "Exit", self)
        closeApplication.setShortcut("Ctrl+Q")
        closeApplication.triggered.connect(self.exitApplication)
        fileMenu.addAction(closeApplication)

        aboutApplication = QAction(QIcon("about.png"), "About App", self)
        aboutApplication.triggered.connect(self.player_widget.aboutMessage)
        helpMenu.addAction(aboutApplication)
        # toolbar Area
        toolbar = self.addToolBar("Toolbar")
        toolbar.addAction(opneFile)
        toolbar.addAction(closeApplication)
        toolbar.addAction(aboutApplication)

    def exitApplication(self):
        self.close()


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        # ============= Design component create  ============
        self.filename_label = QLabel("Open A PDF File First")  # Creat Label
        self.filename_label.setStyleSheet("color: green")
        self.filename_label.setFont(QFont("Arial",20))
        self.total_page_label = QLabel(" ")
        self.total_page_label.setStyleSheet("color: blue")
        self.total_page_label.setFont(QFont("Arial", 14))
        self.editor = QTextEdit()
        # self.aboutButton = QPushButton("About")  # Creat Button
        self.playButton = QPushButton(QIcon("play.png"),"Play")
        self.playButton.setFont(QFont("Arial", 15))
        # self.openButton = QPushButton("Open")
        # self.pauseButton = QPushButton("Pause")
        self.start_page = QLineEdit()  # Create Text input box
        self.end_page = QLineEdit()
        self.label = QLabel("To")

        self.h2_layout = QHBoxLayout()  # Create a Horizontal box layout
        self.h2_layout.addWidget(self.start_page)  # add label in layout
        self.h2_layout.addWidget(self.label)
        self.h2_layout.addWidget(self.end_page)

        # set play pause and open button in Horizontal box
        self.h_layout = QHBoxLayout()
        # self.h_layout.addWidget(self.openButton)
        # self.h_layout.addWidget(self.pauseButton)
        self.h_layout.addWidget(self.playButton)
        # self.h_layout.addWidget(self.aboutButton)

        # Vertical box layout as Main layout
        self.v_layout = QVBoxLayout()  # Create Vertical box layout
        self.v_layout.addWidget(self.filename_label)
        self.v_layout.addLayout(self.h2_layout)  # add horizontal box layout as sub layout

        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addWidget(self.total_page_label)
        self.v_layout.addWidget(self.editor)  # setWindow Title
        self.setLayout(self.v_layout)  # set Layout

        # connect all functional buttons
        # self.aboutButton.clicked.connect(self.aboutMessage)
        self.playButton.clicked.connect(self.play_file)
        # self.openButton.clicked.connect(self.open_file)
        # self.pauseButton.clicked.connect(self.pause_file)

    # ======== button action functions ===================
    # def clear_file(self):
    #     self.start_page.clear()  # clear input box text
    #     self.end_page.clear()

    def play_file(self):
        start = int(self.start_page.text()) or 1
        end = int(self.pages) or int(self.end_page.text())
        self.filename_label.setText("Playing::" + self.filename_label.text())

        for num in range(start, self.pages):
            page = self.pdfReader.getPage(num)  # get page
            text = page.extractText()  # get entire page text format
            self.editor.setText(text)
            self.speaker.say(text)  # speck text
            self.speaker.runAndWait()

    def open_file(self):
        file_name = QFileDialog.getOpenFileName(self, "Open File", "C://", "PDF files (*.pdf) ;;All Files()")
        self.book_name = open(file_name[0], 'rb')  # open PDF file
        self.pdfReader = PyPDF2.PdfFileReader(self.book_name)  # init PyPDF2 by PDF
        self.speaker = pyttsx3.init()  # init pyttsx3
        self.pages = self.pdfReader.numPages  # get total pages
        self.total_page_label.setText("Total Pages: " + str(self.pages))
        head, tail = os.path.split(file_name[0])
        self.filename_label.setText(tail)
        self.start_page.setText("1")
        self.end_page.setText(str(self.pages))
        # self.show()  # Show window

    def aboutMessage(self):
        message = QMessageBox.about(self, "About AudioBook",
                                    "This is PDF Voice Reader \n Version: 1.0.1 \n Build: 02 \n Develop by: Shamsul Haq")


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())  # exit Window
