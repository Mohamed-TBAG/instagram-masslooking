from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from os import path
import sys
#
import requests
import json
from datetime import datetime
import uicodes
#FORM_CLASS=loadUiType("myIDM.ui")[0]

FORM_CLASS,_=loadUiType(path.join(path.dirname(__file__),"form.ui"))
se = requests.Session()

class TBAGx(QMainWindow,FORM_CLASS):
    idess = []
    def __init__(self,parent=None):
        super(TBAGx,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        #must strat with it
        self.UI() #for runnig the changed effects on the UI
        self.buttons()


#Ui defaults
    def UI(self):#ui propertes
        self.setWindowTitle("TBAGidm") #title
        self.setFixedSize(597,274) #desable form resize
        
        self.tabWidget.tabBar().setVisible(False)
        self.pushButton.setVisible(False)
        self.pushButton_2.setVisible(False)
        self.tabWidget.setCurrentIndex(0)
        #secure and tow factor cetion
        self.lineEdit_4.setVisible(False)#tow fac
        self.pushButton_7.setVisible(False)#tow fac
        self.lineEdit_5.setVisible(False)#Secure
        self.pushButton_8.setVisible(False)#Secure
        QApplication.processEvents()
    
    def buttons(self):
        self.pushButton_4.clicked.connect(self.first_tab)#login button
        self.pushButton_3.clicked.connect(self.grabber)#grab button
        self.pushButton_6.clicked.connect(self.story_id)#start watching
        self.pushButton.clicked.connect(self.tab1)#grabber form
        self.pushButton_2.clicked.connect(self.tab2)#settings form
        
    def first_tab(self):
        
        login_user = self.lineEdit.text()
        login_pass = self.lineEdit_2.text()
        self = self
        loginpost = uicodes.login(login_user,login_pass,se,self)


        
        #done


    def grabber(self):
        users = uicodes.grabber_v1(se,self)#returns users ids list
        self.idess.append(users)
        
        
    def story_id(self):
        
        self=self
        users = self.idess #users ids list 
        story_watch = uicodes.story_id_grabber(users,se,self)
        #print(grab_ides)

            
    def tab1(self):
        self.tabWidget.setCurrentIndex(1)
    def tab2(self):
        self.tabWidget.setCurrentIndex(2)


def main():
    app = QApplication(sys.argv)
    window = TBAGx()
    window.show()
    app.exec_()
    


if __name__ == ("__main__"):
    main()

    

