quantity = int(input("how many numbers? "))
interval = int(input("what interval? "))
list = []

for i in range(1, (quantity*interval + 1), interval):
    list.append(i)

print(list)