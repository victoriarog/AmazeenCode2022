info = ["Victoria", "Rogatinskaya", "Front End BSci"]

number = int(input("Enter 1 for name, 2 for name + surname and 3 for full name and degree: "))

if number == 1:
    print(info[0])
elif number == 2:
    print(info[0], info[1])
elif number == 3:
    print(info[0], info[1], info[2])