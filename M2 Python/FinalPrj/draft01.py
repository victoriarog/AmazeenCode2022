import random
import json

# races = ["Human", "Dwarf", "Halfling", "Elf", "Tiefling", "Orc"]
# classes = ["Fighter", "Wizard", "Rogue", "Druid", "Barbarian", "Sorcerer", "Bard", "Cleric", "Monk", "Paladin"]
# genders = ["Male", "Female", "N/A"]

# ability score calculator-ish????

def __getAbilityScores__():
    scores = []
    for i in range(6):
        score = []
        for j in range(4): 
            score.append(random.randint(1,6))

        score = sorted(score)
        score.pop(0) #removing the smallest value score
        scores.append(sum(score)) # and summing all the values together and saving them above

    scores = sorted(scores)
    characterScores = {'STR':0,'DEX':0,'CON':0,'INT':0,'WIS':0,'CHA':0}
    return(scores)

    # match characterClass: #hard coded for now to test ig 
    #     case "Fighter":
    #         characterScores["STR"] = scores[5]
    #         characterScores["CON"] = scores[4]
    #         characterScores["DEX"] = scores[3]
    #         characterScores["WIS"] = scores[2]
    #         characterScores["CHA"] = scores[1]
    #         characterScores["INT"] = scores[0]

    #     case "Wizard":
    #         characterScores["INT"] = scores[5]
    #         characterScores["CON"] = scores[4]
    #         characterScores["DEX"] = scores[3]
    #         characterScores["WIS"] = scores[2]
    #         characterScores["CHA"] = scores[1]
    #         characterScores["STR"] = scores[0]
    #     case "Rogue":
    #         characterScores["DEX"] = scores[5]
    #         characterScores["CON"] = scores[4]
    #         characterScores["WIS"] = scores[3]
    #         characterScores["CHA"] = scores[2]
    #         characterScores["INT"] = scores[1]
    #         characterScores["STR"] = scores[0]

    # return characterScores


# loading the json data

# data = open('/Users/victoriarogatinskaya/Desktop/AmazeenCode2022/M2 Python/FinalPrj/data.json')
# load = json.load(data)

# for i in load['races']:
#     print(i)

# for j in load['classes']:
#     print(j)


# data.close() # loads ok 

# character class to store data

class playerCharacter:
    def __init__(self):
        self.name = " "
        self.age = " "
        self.race = " "
        self.charClass = " " #class isn't a WORD TO USE
        self.abilityScores = " "

#TESTING AREA

# newCharacter.name = "Alex" 
# newCharacter.charClass = "Wizard"
# newCharacter.abilityScores = __getAbilityScores__("Wizard") #test test test

# INPUT TESTING

newCharacter = playerCharacter()

# newCharacter.name = input("Input the character name: ")
# newCharacter.age = input("Choose your character age: ")
# newCharacter.race = input("Choose your character's race: ")
# newCharacter.charClass = input("What's your character class: ")
# newCharacter.abilityScores = __getAbilityScores__(newCharacter.charClass)

print(__getAbilityScores__())
print(f"Here's your basic character sheet: ")
print(vars(newCharacter))