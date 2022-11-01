# print(1, end=' ')
# print(2, end=' ')
# print(3, end=' ')
# print(4, end=' ')
# print(5, end=' ')

# print()


for j in range(1,6, 2):
    for i in range (j+1, j+11):
        # print(i + 1, end=' ')
        if i % 2 == 0:
            print(i-1, end=' ')
    print()
