numbers = []

askNum = int(input("How many numbers will be in an array? "))

for i in range(0, askNum):
    i = int(input("Input your numbers?"))
    numbers.append(i)

for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
      if numbers[j] > numbers[j + 1]:
        t = numbers[j]
        numbers[j] = numbers[j+1]
        numbers[j+1] = t
    print(numbers)