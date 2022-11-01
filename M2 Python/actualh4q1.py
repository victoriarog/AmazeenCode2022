f = open("hw4-numbers.txt", "r") 
text = f.read()
lines = text.split()

for line in lines:
    print(int(line))

# ??????