import sys
from PyQt5 import QtWidgets, uic
import random

from App import Ui_DnDStuff
from Form import Ui_Form

class Popup(QtWidgets.QWidget, Ui_Form):
    def __init__(self, *args, obj=None, **kwargs):
        super(Popup, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.disName.setText(nameSet)
        self.disAge.setText(ageSet)
        self.disRace.setText(raceSet)
        self.disClass.setText(classSet)

        self.disSTR.display(disSetSTR)
        self.disCON.display(disSetCON)
        self.disDEX.display(disSetDEX)
        self.disINT.display(disSetINT)
        self.disWIS.display(disSetWIS)
        self.disCHA.display(disSetCHA)


    


class App(QtWidgets.QMainWindow, Ui_DnDStuff):
    def __init__(self, *args, obj=None, **kwargs):
        super(App, self).__init__(*args, **kwargs)
        self.setupUi(self)

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
        global disSetSTR
        disSetSTR = self.matchyMatch(setSTR)
        return setSTR, disSetSTR

    def setCON(self):
        global setCON
        setCON = self.Constituition.currentText()
        self.numCON.display(self.matchyMatch(setCON))
        global disSetCON
        disSetCON = self.matchyMatch(setCON)
        return setCON, disSetCON

    def setDEX(self):
        global setDEX
        setDEX = self.Dexterity.currentText()
        self.numDEX.display(self.matchyMatch(setDEX))
        global disSetDEX
        disSetDEX = self.matchyMatch(setDEX)
        return setDEX, disSetDEX

    def setINT(self):
        global setINT
        setINT = self.Intelligence.currentText()
        self.numINT.display(self.matchyMatch(setINT))
        global disSetINT
        disSetINT = self.matchyMatch(setINT)
        return setINT, disSetINT

    def setWIS(self):
        global setWIS
        setWIS = self.Wisdom.currentText()
        self.numWIS.display(self.matchyMatch(setWIS))
        global disSetWIS
        disSetWIS = self.matchyMatch(setWIS)
        return setWIS, disSetWIS

    def setCHA(self):
        global setCHA
        setCHA = self.Charisma.currentText()
        self.numCHA.display(self.matchyMatch(setCHA))
        global disSetCHA
        disSetCHA = self.matchyMatch(setCHA)
        return setCHA, disSetCHA

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

        self.window = Popup()
        self.window.show()


app = QtWidgets.QApplication(sys.argv)

window = App()
window.show()
app.exec()