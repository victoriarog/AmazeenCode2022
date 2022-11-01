sumOutput = 0

while True:
    number = int(input("Please, input a number between 0 and 100: ")) 
    if 10 <= number <= 20:
        sumOutput += number
    elif 10 > number and number > 20:
        pass
    elif number > 100:
        pass
    elif number == 0:
        break
 
print("The total sum is ", sumOutput)
