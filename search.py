# Erfanullah Arsala and Joel Terran
# 11/20/2019
# Homework 3: Image Search
# Abstract: A GUI that prompts a user to select a image filter option
# and a search bar to enter information about
# picture and once "Search" (thanks to cookie and Erik for helping me this part) button is clicked 
# the code will search through a dictionary of images
# to find the image with the best matching tags 
# FYI: All images have to be in same directory as python file

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                                QLineEdit, QHBoxLayout, QVBoxLayout, QDialog,
                                QTextBrowser, QComboBox)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSlot, QUrl
from PyQt5.QtGui import QColor
from PIL import Image

# im1 = Image.open("34694102243_3370955cf9_z.jpg")
# im2 = Image.open("37198655640_b64940bd52_z.jpg")
# im3 = Image.open("36909037971_884bd535b1_z.jpg")
# im4 = Image.open("36604481574_c9f5817172_z.jpg")
# im5 = Image.open("36885467710_124f3d1e5d_z.jpg")
# im6 = Image.open("37246779151_f26641d17f_z.jpg")
# im7 = Image.open("36523127054_763afc5ed0_z.jpg")
# im8 = Image.open("35889114281_85553fed76_z.jpg")
# im9 = Image.open("34944112220_de5c2684e7_z.jpg")
# im10 = Image.open("36140096743_df8ef41874_z.jpg")

# pics = [im1, im2, im3, im4, im5, im6, im7, im8, im9, im10]

#dropdown part
url_list = [
    'Pick a value',
    'Sepia',
    'Negative',
    'Grayscale',
    'Thumbnail',
    'None'
] 

#dictionary of images info
image_info = [
     {
           "id" : "34694102243_3370955cf9_z",
           "title" : "Eastern",
           "flickr_user" : "Sean Davis",
           "tags" : ["Los Angeles", "California", "building"]
      },
      {
           "id" : "37198655640_b64940bd52_z",
           "title" : "Spreetunnel",
           "flickr_user" : "Jens-Olaf Walter",
           "tags" : ["Berlin", "Germany", "tunnel", "ceiling"]
      },
      {
           "id" : "36909037971_884bd535b1_z",
           "title" : "East Side Gallery",
           "flickr_user" : "Pieter van der Velden",
           "tags" : ["Berlin", "wall", "mosaic", "sky", "clouds"]
      },
      {
           "id" : "36604481574_c9f5817172_z",
           "title" : "Lombardia, september 2017",
           "flickr_user" : "Mónica Pinheiro",
           "tags" : ["Italy", "Lombardia", "alley", "building", "wall"]
      },
      {
           "id" : "36885467710_124f3d1e5d_z",
           "title" : "Palazzo Madama",
           "flickr_user" : "Kevin Kimtis",
           "tags" : [ "Rome", "Italy", "window", "road", "building"]
      },
      {
           "id" : "37246779151_f26641d17f_z",
           "title" : "Rijksmuseum library",
           "flickr_user" : "John Keogh",
           "tags" : ["Amsterdam", "Netherlands", "book", "library", "museum"]
      },
      {
           "id" : "36523127054_763afc5ed0_z",
           "title" : "Canoeing in Amsterdam",
           "flickr_user" : "bdodane",
           "tags" : ["Amsterdam", "Netherlands", "canal", "boat"]
      },
      {
           "id" : "35889114281_85553fed76_z",
           "title" : "Quiet at dawn, Cabo San Lucas",
           "flickr_user" : "Erin Johnson",
           "tags" : ["Mexico", "Cabo", "beach", "cactus", "sunrise"]
      },
      {
           "id" : "34944112220_de5c2684e7_z",
           "title" : "View from our rental",
           "flickr_user" : "Doug Finney",
           "tags" : ["Mexico", "ocean", "beach", "palm"]
      },
      {
           "id" : "36140096743_df8ef41874_z",
           "title" : "Someday",
           "flickr_user" : "Thomas Hawk",
           "tags" : ["Los Angeles", "Hollywood", "California", "Volkswagen", "Beatle", "car"]
      }
]

# #sepia function to apply sepia filter to image
# def sepia(picture):
#     def mypic(p):
#         #increase red
#         if p[0] < 63:
#             r,g,b = int(p[0] * 1.5), p[1], int(p[2] * 0.9)
#         elif p[0] > 62 and p[0] < 192:
#             r,g,b = int(p[0] * 1.15), p[1], int(p[2] * 0.85)
#         else:
#             r = int(p[0] * 1.08)
#             if r > 255:
#                 r = 255
#             g,b = p[1], int(p[2] * 0.5)
#         return r, g, b

#     new = map(mypic, picture.getdata())
#     picture.putdata(list(new))
#     picture.show()

# #negative function to apply negative filter to image
# def negative(picture):
#     newList = []
#     for p in picture.getdata():
#         # reduce the green and blue channel by multiplying by .70 and getting integer value of that
#         temp = (p[0], int(p[1] * .20), int(p[2]* .60))
#         # overwrite list and add new values to the list
#         newList.append(temp)
#         # all data from picture is replaced with newList data
#     picture.putdata(newList)
#     # save the new picture with reduced green and blue channel values
#     picture.show()

# # greyscale function to apply greyscale filter to image
# def greyscale(picture):
#     image = Image.open(picture).convert('LA')
#     image.show()

# # thumbnail function to apply thumbnail filter to image
# def thumbnail(picture):   
#     image = Image.open(picture) 
#     size = (100, 100)
#     #call thumbnail to resize image 
#     image.thumbnail(size) 
#     image.show()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Find Image: ")
        self.label2 = QLabel("Image Filter:")
        self.line_edit = QLineEdit()
        self.combo_box = QComboBox()
        self.combo_box.addItems(url_list)
        self.search = QPushButton("Search")
        #apply vbox layout
        vbox = QVBoxLayout()
        #add "image filter"
        vbox.addWidget(self.label2)
        #add dropdown
        vbox.addWidget(self.combo_box)
        #add "find image"
        vbox.addWidget(self.label)
        #add search line
        vbox.addWidget(self.line_edit)
        #add "search" button
        vbox.addWidget(self.search)
        self.setLayout(vbox)
        self.setWindowTitle("Homework 3: Image Search")
        self.search.clicked.connect(self.new_win)

        for i in range(10):
            #convert titles and tags into lower case
            image_info[i]["title"] = image_info[i]["title"].split()
            image_info[i]["title"] = [x.lower() for x in image_info[i]["title"]]
            image_info[i]["tags"] = [x.lower() for x in image_info[i]["tags"]]
    @pyqtSlot()
    def new_win(self):
        self.combo_box.currentText()
        text = self.line_edit.text()
        count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        super().__init__()
        text = text.split()
        #change item to lowercase
        text = [item.lower() for item in text]
        print(text)
        for word in text:
            print(word)
            for item in range(len(image_info)):
                if(word in image_info[item]["tags"] or word in image_info[item]["title"]):
                    count[item] += 1
        keeping_count = []
        #get max numbers
        for num in range(len(count)):
            if(count[num] == max(count)):
                keeping_count.append((image_info[num]["title"][0], num)) 
        #sort the list after appending the tuple          
        sort = sorted(keeping_count)
        print(sort)
        index = (sort[0][1])
        im = Image.open(image_info[index]["id"] + ".jpg")


        #get index of what the person chooses on the list
        i = self.combo_box.currentIndex()
        if i!=0:
            #sepia function to apply sepia filter to image
            if i == 1:
                newList = []
                for pic in im.getdata():
                    temp = (pic[0], int(pic[1]*.7), int(pic[2]*.7))
                    newList.append(temp)
                im.putdata(newList)
                im.show()

            #negative function to apply negative filter to image
            elif i == 2:
                picture = im
                newList = []
                for p in picture.getdata():
                    # reduce the green and blue channel by multiplying by .70 and getting integer value of that
                    temp = (p[0], int(p[1] * .20), int(p[2]* .60))
                    # overwrite list and add new values to the list
                    newList.append(temp)
                # all data from picture is replaced with newList data
                picture.putdata(newList)
                # save the new picture with reduced green and blue channel values
                picture.show()

            # greyscale function to apply greyscale filter to image    
            elif i == 3:
                image = im.convert('LA')
                image.show()

            # thumbnail function to apply thumbnail filter to image
            elif i == 4:
                size = (250, 250)
                im.thumbnail(size)
                im.show()
            #if they choose none just open up the image
            else:
                im.show()

app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())