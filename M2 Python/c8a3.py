dict = {
    'thanks' : 'gracias',
    'sorry' : 'persona',
    'hello' : 'hola',
    'goodbye' : 'adios',
    'table' : 'mesa',
    'dog' : 'perrito'
}

# while True: 
#     word = input("put your word here? ")

#     if word in dict:
#         print(f'translation is {dict[word]}')
#     else: 
#         print(f"not found, try again")

while True:
    print()
    sentence = input(f"give me a text: ")
    words = sentence.split(' ')

    for word in words:
        if word in dict:
            print(dict[word], end = ' ')
        else: 
            print(f"nope, no words like that here")
