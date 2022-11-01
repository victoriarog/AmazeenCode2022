max = int(input("Please, input the maximal value: "))
div = int(input("Please, input the divisor value: "))

for i in range(1, max + 1):
    if i % div == 0:
        print(i)
    else: pass