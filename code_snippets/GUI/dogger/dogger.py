'''
Frederick Herzog
10-29-21
Dogger
'''

from PyQt5.QtWidgets import QMainWindow, QWidget, \
    QPushButton, QLabel, QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap, QIcon, QPalette
from PyQt5.QtCore import Qt
from requests import request, get
from sys import platform, exit, argv
from random import randint
#import pymongo
import json
import os


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # setting  the geometry of window
        self.setGeometry(900, 400, 500, 400)
        self.setStyleSheet("background-color: gray;")
        self.title = "Dogger"
        self.icon_path = 'images/icons/doge.png'
        self.setWindowIcon(QIcon(self.icon_path))
        self.setWindowTitle(self.title)
        self.layout = QVBoxLayout()
        self.button = QPushButton(self)
        self.button.setGeometry(200, 5, 250, 20)
        self.button.setText("CLICK ME! \U0001F606")
        self.button.setStyleSheet("background-color: white;")
        self.label = QLabel(self)
        self.button.clicked.connect(self.requestdoge)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        self.show()

    def requestdoge(self):
        resp = request("GET", "https://dog.ceo/api/breeds/image/random")
        j = json.loads(resp.text)
        # print(j)
        url = j['message']
        # print(url)
        breed = url.split("/")[4]
        img_name = url.split("/")[5]
        ext = img_name[-4:]
        # print(breed)
        # print(img_name)

        # Download the image to images directory
        if platform == "linux" or platform == "linux2" or platform == "darwin":
            img_data = get(url).content
            img_folder = "images/dog"
            # print(img_path)
            files = os.listdir()
            rename = f'{breed}{ext}'
            if rename in files:
                rename = f'{breed}-{randint(1,60)}{ext}'
            img_path = os.path.join(img_folder, rename)
            with open(img_path, 'wb') as handler:
                handler.write(img_data)
        elif platform == "win32":
            pass

        # Change text inside push button to breed
        self.button.setText(breed)

        # Display the image
        if os.path.isfile(img_path):
            # print("True")
            # self.label.clear()
            pixmap = QPixmap(img_path)
            self.label.setPixmap(pixmap)
            #self.resize(pixmap.width(), pixmap.height())
            self.widget = QWidget()
            self.widget.setLayout(self.layout)
            self.setCentralWidget(self.widget)

        # Store the record
        record = {breed: rename}
        print(record)
        # try:
        #     myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        #     mydb = myclient["mydatabase"]
        #     mycol = mydb["dogs"]
        #     x = mycol.insert_one(record)
        # except:
        #     pass

        def resizeImage():
            pass


if __name__ == '__main__':
    # create pyqt5 a# Only needed for access to command line argumentspp
    App = QApplication(argv)
    # create the instance of our Window
    window = Window()
    '''
    start the app

        You need one (and only one) QApplication instance per application.
        Pass in sys.argv to allow command line arguments for your app.
        If you know you won't use command line arguments QApplication([]) works too.
    '''
    #window.resize(800, 800)
    exit(App.exec())
