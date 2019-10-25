import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QHBoxLayout, QLineEdit
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QColor, QPixmap
from PIL import Image, ImageOps
# Authors:Erik Gallardo-Cruz and Guillermo Flores
# Date: October 17, 2019
# Course: CST 205
# Description: This code will take in a user input and a filter option
# from a list. When the user submits, the program will find the image closest
#  This is a list of choices we can choose from
my_filters = ["Pick a filter",
          "Sepia",
          "Negative",
          "Grayscale",
          "Thumbnail",
          "None"]

image_info = [
     {
           "id" : "images/34694102243_3370955cf9_z.jpg",
           "title" : "Eastern",
           "flickr_user" : "Sean Davis",
           "tags" : ["Los Angeles", "California", "building"],
      },
      {
           "id" : "images/37198655640_b64940bd52_z.jpg",
           "title" : "Spreetunnel",
           "flickr_user" : "Jens-Olaf Walter",
           "tags" : ["Berlin", "Germany", "tunnel", "ceiling"]
      },
      {
           "id" : "images/36909037971_884bd535b1_z.jpg",
           "title" : "East Side Gallery",
           "flickr_user" : "Pieter van der Velden",
           "tags" : ["Berlin", "wall", "mosaic", "sky", "clouds"]
      },
      {
           "id" : "images/36604481574_c9f5817172_z.jpg",
           "title" : "Lombardia, september 2017",
           "flickr_user" : "Mónica Pinheiro",
           "tags" : ["Italy", "Lombardia", "alley", "building", "wall"]
      },
      {
           "id" : "images/36885467710_124f3d1e5d_z.jpg",
           "title" : "Palazzo Madama",
           "flickr_user" : "Kevin Kimtis",
           "tags" : [ "Rome", "Italy", "window", "road", "building"]
      },
      {
           "id" : "images/37246779151_f26641d17f_z.jpg",
           "title" : "Rijksmuseum library",
           "flickr_user" : "John Keogh",
           "tags" : ["Amsterdam", "Netherlands", "book", "library", "museum"]
      },
      {
           "id" : "images/36523127054_763afc5ed0_z.jpg",
           "title" : "Canoeing in Amsterdam",
           "flickr_user" : "bdodane",
           "tags" : ["Amsterdam", "Netherlands", "canal", "boat"]
      },
      {
           "id" : "images/35889114281_85553fed76_z.jpg",
           "title" : "Quiet at dawn, Cabo San Lucas",
           "flickr_user" : "Erin Johnson",
           "tags" : ["Mexico", "Cabo", "beach", "cactus", "sunrise"]
      },
      {
           "id" : "images/34944112220_de5c2684e7_z.jpg",
           "title" : "View from our rental",
           "flickr_user" : "Doug Finney",
           "tags" : ["Mexico", "ocean", "beach", "palm"]
      },
      {
           "id" : "images/36140096743_df8ef41874_z.jpg",
           "title" : "Someday",
           "flickr_user" : "Thomas Hawk",
           "tags" : ["Los Angeles", "Hollywood", "California", "Volkswagen", "Beatle", "car"]
      }
]

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.label1 = QLabel("Image Search: ")
        self.line_edit = QLineEdit()
        hbox = QHBoxLayout()
        hbox.addWidget(self.label1)
        hbox.addWidget(self.line_edit)

        self.combo_box = QComboBox()
        self.combo_box.addItems(my_filters)
        self.submit = QPushButton('Submit')
        vbox = QVBoxLayout()
        vbox.addWidget(self.combo_box)
        vbox.addWidget(self.submit)

        mbox = QVBoxLayout()
        mbox.addLayout(hbox)
        mbox.addLayout(vbox)

        self.setLayout(mbox)
        self.submit.clicked.connect(self.new_win)
        self.setWindowTitle("Image Search")

        # This converts both the titles and tags of the dictionary into lower case
        # Case sensitive
        for i in range(10):
            image_info[i]["title"] = image_info[i]["title"].split()
            image_info[i]["tags"] = [x.lower() for x in image_info[i]["tags"]]
            image_info[i]["title"] = [x.lower() for x in image_info[i]["title"]]

    @pyqtSlot()
    def new_win(self):
        my_filter = self.combo_box.currentText()
        my_text = self.line_edit.text()

        points = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        super().__init__()
        text_list = my_text.split()
        text_list = [item.lower() for item in text_list]  # This will transorm the list input into lowercases
        print(text_list)
        for word in text_list:
            print(word)
            for item in range(len(image_info)):
                if(word in image_info[item]["tags"] or word in image_info[item]["title"]):
                    points[item] += 1

        max_points = []
        for num in range(len(points)):  # We do this so we can create a list of only the max numbers.
            if(points[num] == max(points)):
                max_points.append((image_info[num]["title"][0], num))  # This appends a tuple with the first word of the title and the index.
        sorted_max = sorted(max_points)
        print(sorted_max)
        index_points = (sorted_max[0][1])
        print(points)
        im = Image.open(image_info[index_points]["id"])

        #Once an image is chosen with chooser, we will apply
        #a filter to it.

        if (my_filter == "Sepia"):
            new_list = []
            for p in im.getdata():
                temp = (p[0], int(p[1]*.7), int(p[2]*.7))
                new_list.append(temp)
            im.putdata(new_list)
            im.save('images/sepia.jpg')
            newIM = Image.open('images/sepia.jpg')
            newIM.show()
        if (my_filter == "Negative"):
            ImageOps.invert(im).show()
        elif (my_filter == "Grayscale"):
            im.convert('LA').show()
        elif (my_filter == "Thumbnail"):
            size = (128, 128)
            im.thumbnail(size)
            im.save('images/thumbnail.jpg')
            newIM = Image.open('images/thumbnail.jpg')
            newIM.show()
        elif (my_filter == "None"):
            im.show()

app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())