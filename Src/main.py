import os
import sys
import pyttsx3
import PyPDF2
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout, QFileDialog, QLabel, QPushButton, QLineEdit)

book_name = open('python_tutorial.pdf','rb')  #open PDF file
pdfReader =PyPDF2.PdfFileReader(book_name) # init PyPDF2 by PDF
speaker = pyttsx3.init() # init pyttsx3
pages = pdfReader.numPages  # get total pages

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.filename_label = QLabel("Python Tutorial.pdf")
        self.total_page_label = QLabel(" ")
        self.clearButton = QPushButton("Clear")
        self.playButton = QPushButton("Play")
        self.start_page = QLineEdit()
        self.end_page = QLineEdit()
        self.label = QLabel("To")

        self.h2_layout = QHBoxLayout()
        self.h2_layout.addWidget(self.start_page)
        self.h2_layout.addWidget(self.label)
        self.h2_layout.addWidget(self.end_page)

        #set paly pause and open buttom in H
        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.playButton)
        self.h_layout.addWidget(self.clearButton)


        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.filename_label)
        self.v_layout.addLayout(self.h2_layout)
        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addWidget(self.total_page_label)

        self.setWindowTitle("Audio Book")
        self.setLayout(self.v_layout)

        # connect all functional buttons
        self.clearButton.clicked.connect(self.clear_file)
        self.playButton.clicked.connect(self.play_file)
        self.total_page_label.setText("Total Pages: " + str(pages))
        self.show()

    def clear_file(self):
        self.start_page.clear()
        self.end_page.clear()

    def play_file(self):
        start = int(self.start_page.text()) or 1
        end = int(pages) or int (self.end_page.text())
        self.filename_label.setText("Playing:: Python Tutorial.pdf")
        for num in range(start,pages):
            page = pdfReader.getPage(num)   # get page
            text = page.extractText()     # get entire page text format
            speaker.say(text)          # speck text
            speaker.runAndWait()


app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())