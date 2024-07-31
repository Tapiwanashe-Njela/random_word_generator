#Import modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout #AWLPVH
from random import choice #allows us to choose a random word from a list


#Main app,create objects and settings
app = QApplication([])  #Allows us to create and execute our app; takes in an empty list ALWAYS
main_window = QWidget() #Object to create a new form (window) that we will be editing
main_window.setWindowTitle("Random Word Maker") #Now we use the modules methods to alter the appearance 
main_window.resize(300, 200) #Adjusting the size of the form

#Create all app objects
title = QLabel("Random Keywords")

text1 = QLabel("?")
text2 = QLabel("?")
text3 = QLabel("?")

button1 = QPushButton("Click me")
button2 = QPushButton("Click me")
button3 = QPushButton("Click me")

my_words = ["calculate", "goodbye", "maybe", "hello", "how", "are", "you", "bye"]

#ALL DESIGN HERE; Getting all the created objects onto our screen
master_layout = QVBoxLayout() #Creates a column 

row1 = QHBoxLayout() #Creates a row
row2 = QHBoxLayout() #Creates a row
row3 = QHBoxLayout() #Creates a row

#Add the objects to the layout using addWidget method; here we can edit the appearance
row1.addWidget(title, alignment=Qt.AlignCenter) #Add a widget; here we add the title label with alignment at the center 

row2.addWidget(text1, alignment=Qt.AlignCenter) #Here we add the title label with alignment at the center 
row2.addWidget(text2, alignment=Qt.AlignCenter) #Here we add the title label with alignment at the center 
row2.addWidget(text3, alignment=Qt.AlignCenter) #Here we add the title label with alignment at the center 

row3.addWidget(button1) #Buttons do not need alignment
row3.addWidget(button2)
row3.addWidget(button3)

#Drop the layouts to the master layout; e.g rows and columns are layouts 
master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

main_window.setLayout(master_layout) #We then set the master layout as the main layout

#Create functions
def random_word1(): #selects a random word from word_list using the imported choice module and sets it to text1 label
    word = choice(my_words) 
    text1.setText(word)

def random_word2(): #selects a random word from word_list using the imported choice module and sets it to text2 label
    word = choice(my_words)
    text2.setText(word)

def random_word3(): #selects a random word from word_list using the imported choice module and sets it to text3 label
    word = choice(my_words)
    text3.setText(word)

#Events
button1.clicked.connect(random_word1) #connect the random word function to the button1 clicked event
button2.clicked.connect(random_word2) #connect the random word function to the button2 clicked event
button3.clicked.connect(random_word3) #connect the random word function to the button3 clicked event

#Show and run the app
main_window.show() #Display the form 
app.exec_() #Run the app