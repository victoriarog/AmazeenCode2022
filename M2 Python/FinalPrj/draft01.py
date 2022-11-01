import random

# races = ["Human", "Dwarf", "Halfling", "Elf", "Tiefling", "Orc"]
# classes = ["Fighter", "Wizard", "Rogue", "Druid", "Barbarian", "Sorcerer", "Bard", "Cleric", "Monk", "Paladin"]
# genders = ["Male", "Female", "N/A"]

# ability score calculator-ish????

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

print(scores) #see all random generated values here