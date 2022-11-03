import sys
from PyQt5 import QtWidgets, uic
import random

from App import Ui_DnDStuff




class App(QtWidgets.QMainWindow, Ui_DnDStuff):
    def __init__(self, *args, obj=None, **kwargs):
        super(App, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # set variables

        self.submit.clicked.connect(self.submitAll)

        self.name.editingFinished.connect(self.changeName)
        self.race.activated.connect(self.onActivate)
        self.age.editingFinished.connect(self.changeAge)
        self.classCh.activated.connect(self.onActivateClass)

        self.Strength.activated.connect(self.setSTR)
        self.Constituition.activated.connect(self.setCON)
        self.Dexterity.activated.connect(self.setDEX)
        self.Intelligence.activated.connect(self.setINT)
        self.Wisdom.activated.connect(self.setWIS)
        self.Charisma.activated.connect(self.setCHA)

        # get ability scores from clicking <3 

        self.generate.clicked.connect(self.getAbilityScores)

    def onActivate(self):
        global raceSet
        raceSet = self.race.currentText()
        return raceSet

    def onActivateClass(self):
        global classSet
        classSet = self.classCh.currentText()
        return classSet
        
    def changeName(self):
        global nameSet
        nameSet = self.name.text()
        return nameSet

    def changeAge(self):
        global ageSet
        ageSet = self.age.text()
        return ageSet

    def matchyMatch(self, some):
        global matchy
        if some == "NUM1":
            matchy = scores[0]
        elif some == "NUM2":
            matchy = scores[1]
        elif some == "NUM3":
            matchy = scores[2]
        elif some == "NUM4":
            matchy = scores[3]
        elif some == "NUM5":
            matchy = scores[4]
        elif some == "NUM6":
            matchy = scores[5]
        return matchy

    def setSTR(self):
        global setSTR
        setSTR = self.Strength.currentText()
        self.numSTR.display(self.matchyMatch(setSTR))
        return setSTR

    def setCON(self):
        global setCON
        setCON = self.Constituition.currentText()
        self.numCON.display(self.matchyMatch(setCON))
        return setCON

    def setDEX(self):
        global setDEX
        setDEX = self.Dexterity.currentText()
        self.numDEX.display(self.matchyMatch(setDEX))
        return setDEX

    def setINT(self):
        global setINT
        setINT = self.Intelligence.currentText()
        self.numINT.display(self.matchyMatch(setINT))
        return setINT

    def setWIS(self):
        global setWIS
        setWIS = self.Wisdom.currentText()
        self.numWIS.display(self.matchyMatch(setWIS))
        return setWIS

    def setCHA(self):
        global setCHA
        setCHA = self.Charisma.currentText()
        self.numCHA.display(self.matchyMatch(setCHA))
        return setCHA

    def getAbilityScores(self):
        global scores 
        scores = []
        for i in range(6):
            score = []
            for j in range(4): 
                score.append(random.randint(1,6))

            score = sorted(score)
            score.pop(0)
            scores.append(sum(score))

        scores = sorted(scores)
        
        self.NUM1.display(scores[0])
        self.NUM2.display(scores[1])
        self.NUM3.display(scores[2])
        self.NUM4.display(scores[3])
        self.NUM5.display(scores[4])
        self.NUM6.display(scores[5])

        return scores

       
    def submitAll(self):
        print("Name: " + nameSet)
        print("Age: " + ageSet)
        print("Race: " + raceSet)
        print("Class: " + classSet)
        print(self.matchyMatch(setSTR))
        print(self.matchyMatch(setCON))
        print(self.matchyMatch(setDEX))
        print(self.matchyMatch(setINT))
        print(self.matchyMatch(setWIS))
        print(self.matchyMatch(setCHA))

app = QtWidgets.QApplication(sys.argv)

window = App()
window.show()
app.exec()