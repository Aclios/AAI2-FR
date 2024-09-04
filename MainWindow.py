from PySide6.QtGui import QIcon , QPixmap, QCursor
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox
from PySide6.QtCore import Qt
import utils
import json
import os
import pygame
from patch import NDSPatch
import webbrowser

msg = json.load(open(utils.resource_path(os.path.join('assets','msg.json')),encoding='utf-8'))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        w=350
        h=455
        pygame.init()
        pygame.mixer.music.set_volume(0.1)
        self.setWindowTitle(msg['patchtitle'])
        self.setWindowIcon(QIcon(utils.resource_path(os.path.join('assets','icon.png'))))
        self.resize(w,h)
        self.setFixedSize(self.size())

        logo = self.addimage('logo',(10,10))

        self.addlabel('Sélectionnez un patch à charger:',10,212)
        self.patchpath = self.addlineedit('',(10,235),(250,25))
        explorepatchbutton = self.addpushbutton('Parcourir',(270,235),(70,25))
        explorepatchbutton.clicked.connect(lambda e: self.explorepatch())

        self.addlabel('Sélectionnez la rom à patcher:',10,272)
        self.rompath = self.addlineedit('',(10,295),(250,25))
        explorerombutton = self.addpushbutton('Parcourir',(270,295),(70,25))
        explorerombutton.clicked.connect(lambda e: self.explorerom())

        self.addlabel('Sélectionnez le dossier de destination:',10,332)
        self.distdirpath = self.addlineedit('',(10,355),(250,25))
        exploredistdirbutton = self.addpushbutton('Parcourir',(270,355),(70,25))
        exploredistdirbutton.clicked.connect(lambda e: self.exploredistdir())

        self.applybutton = self.addpushbutton('Appliquer',(100,410),(70,25))
        self.applybutton.clicked.connect(lambda e: self.applypatch())
        self.applybutton.setEnabled(False)

        self.credits = self.addpushbutton('Crédits',(180,410),(70,25))
        self.credits.clicked.connect(lambda e: self.displaycredits())
        self.credits.setEnabled(False)

        aailogo = self.addimage('aaifr.png',(0,400))

        discord = self.addimage('discord.png',(270,410))
        discord.mousePressEvent = lambda e: callback("https://discord.gg/bye98cMs8S")
        discord.setCursor(Qt.PointingHandCursor)

        web = self.addimage('web.png',(310,405))
        web.mousePressEvent = lambda e: callback("https://aai-fr.keuf.net/")
        web.setCursor(Qt.PointingHandCursor)


    def button_control(self):
        if self.patchpath.text() != "":
            self.credits.setEnabled(True)
        else:
            self.credits.setEnabled(False)

        if self.patchpath.text() != "" and self.rompath.text() != "" and self.distdirpath.text() != "":
            self.applybutton.setEnabled(True)
        else:
            self.applybutton.setEnabled(False)


    def addlabel(self,text,x,y):
        label = QLabel(text,self)
        label.move(x,y)
        label.adjustSize()
        label.show()
        return label

    def addpushbutton(self,text,coords,size):
        button = QPushButton(text,self)
        button.move(coords[0],coords[1])
        button.resize(size[0],size[1])
        button.show()
        return button

    def addlineedit(self,text,coords,size):
        lineedit = QLineEdit(self,text)
        lineedit.setReadOnly(True)
        lineedit.move(coords[0],coords[1])
        lineedit.resize(size[0],size[1])
        lineedit.show()
        return lineedit

    def addimage(self,name,coords):
        im = QLabel(self)
        pixmap = QPixmap(utils.resource_path(os.path.join('assets',name)))
        im.setPixmap(pixmap)
        im.move(coords[0],coords[1])
        im.resize(pixmap.width(),pixmap.height())
        im.show()
        return im

    def explorepatch(self):
        utils.playsound('open')
        patchpath = QFileDialog.getOpenFileName(caption="Sélectionnez le patch à charger",filter = ("NDS Patch (*.ndspatch)"))[0]
        try:
            self.patch = NDSPatch(patchpath)
            self.patchpath.setText(patchpath)
            utils.playsound('close')
        except:
            utils.playsound('objection')
            pop = Popup('Erreur',msg["patcherror"])
            pop.exec()
        self.button_control()

    def explorerom(self):
        utils.playsound('open')
        rompath = QFileDialog.getOpenFileName(caption="Sélectionnez la rom à charger",filter = ("NDS ROM (*.nds)"))[0]
        if utils.check_hash(rompath,self.patch.source_hash):
            self.rompath.setText(rompath)
            utils.playsound('close')

        else:
            utils.playsound('objection')
            pop = Popup('Erreur',msg["hasherror"])
            pop.exec()
        self.button_control()

    def exploredistdir(self):
        utils.playsound('open')
        distdirpath = QFileDialog.getExistingDirectory(caption="Sélectionnez le dossier de destination")
        self.distdirpath.setText(distdirpath)
        utils.playsound('close')
        self.button_control()

    def displaycredits(self):
        pop = Popup('Crédits',self.patch.credits)
        pop.setFixedSize(self.size())
        pop.exec()

    def applypatch(self):
        try:
            utils.playsound("takethat")
            self.patch.patch_file(self.rompath.text(),os.path.join(self.distdirpath.text(),msg["gamename"]))
            pop = Popup('Patch appliqué avec succès !',msg["patchconfirm"])
            pop.exec()
        except:
            utils.playsound("objection")
            pop = Popup("Erreur",msg["unknowngamepatcherror"])
            pop.exec()

class Popup(QMessageBox):
    def __init__(self,window_title,text):
        super().__init__()
        self.setWindowTitle(window_title)
        self.setText(text)
        self.setWindowIcon(QIcon(utils.resource_path(os.path.join('assets','icon.png'))))



def callback(url):
   webbrowser.open_new_tab(url)




