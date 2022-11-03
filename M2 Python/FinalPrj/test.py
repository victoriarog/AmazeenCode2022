import sys
from PyQt5 import QtWidgets, uic
import random

from App import Ui_DnDStuff


class App(QtWidgets.QMainWindow, Ui_DnDStuff):
    def __init__(self, *args, obj=None, **kwargs):
        super(App, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # submit bttn 

        # self.submit.clicked.connect(self.submitAll)

    # def submitAll():



        # get ability scores from clicking <3 

        self.generate.clicked.connect(self.getAbilityScores)

        #set class and race  NEEDS WORK 

        self.race.activated.connect(self.onActivate)

    def onActivate(self):
        raceSet = self.race.currentText()
        print(raceSet)


        self.classCh.activated.connect(self.onActivateClass)

    def onActivateClass(self):
        classSet = self.classCh.currentText()
        print(classSet)

        # display chosen numbers NEEDS WORK

        strSet = self.STR.currentText()
        self.numSTR.display(strSet)

        conSet = self.CON.currentText()
        self.numCON.display(conSet)

        dexSet = self.DEX.currentText()
        self.numDEX.display(dexSet)

        intSet = self.INT.currentText()
        self.numINT.display(intSet)

        wisSet = self.WIS.currentText()
        self.numWIS.display(wisSet)

        chaSet = self.CHA.currentText()
        self.numCHA.display(chaSet)

        #set name and age

        self.name.editingFinished.connect(self.changeName)

    def changeName(self):
        nameSet = self.name.text()
        print(nameSet) # test print

        self.age.editingFinished.connect(self.changeAge)

    def changeAge(self):
        ageSet = self.age.text()
        print(ageSet) # test print

    def getAbilityScores(self):
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


app = QtWidgets.QApplication(sys.argv)

window = App()
window.show()
app.exec()