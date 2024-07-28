#Import modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout #AWLPV

#Main app,create objects and settings
app = QApplication([])  #Allows us to create and execute our app
main_window = QWidget  #These are the forms (windows) we will be editing
main_window.setWindowTitle("Random Word Maker") #Now we use the modules methods to alter
main_window.resize(300, 200) #Adjusting the size of the form

#Create all app objects

#--->    ALL DESIGN HERE  <---

#Events

#Show and run the app
main_window.show() #Display the form 
app.exec_() #Run the app