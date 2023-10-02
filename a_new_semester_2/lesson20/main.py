import random

# a = 5

# while a != 0:
#     print(a)
#     a -= 1


# while True:
#     username = input('Enter your name: ')
#     if username == '0':
#         break
#     else:
#         print(username)

# b = ['Good morning', 'Good day', 'Good afternoon']

# a = random.choice(b)
# random_number = random.randint(15, 20)
# random_range = random.randrange(0, 20)

# print(random_range)
# print(random_number)

# print(a)

# def greeting(name, number, second_number, *args, **kwargs):
#     greetings_string = f'Hello {name}!'
#     print('Args -', args)
#     print('Kwargs -', kwargs)
#     result = [greetings_string, number, second_number, sum(args), kwargs]
#     return result


# a = greeting('Yaroslav', 1,2,3,4,5,22,23,45,76, a=7, b='John', c=15)
# print(a)

# print(list(range(0,5,-1)))

# numbers = [ 6, 2, 1, 8, 10 ]

# def func(list):
#     result = {
#         'sum_of_max_and_min': max(list) + min(list),
#         'sum_of_the_rest': sum(list) - (max(list) + min(list))
#     }
#     return result


# print(func(numbers))


# file = open('lessons/lesson20/test.txt', 'w')
# symbols_written = file.write('hello!')
# print(symbols_written)
# file.close()

# file = open('lessons/lesson20/test.txt', 'w+')
# file.write('hello!')
# file.seek(0)

# first_two_symbols = file.read(2)
# print(first_two_symbols)
# file.close()

# file = open('lessons/lesson20/test.txt', 'w')
# file.write('HELLO!\nWORLD!')
# file.close()

# file = open('lessons/lesson20/test.txt', 'r')
# all_file = file.read()
# print(all_file)
# file.close()

#file = open('lessons/lesson20/test.txt', 'w')
#file.write('HELLO!\nWORLD!')
#file.close()

#file = open('lessons/lesson20/test.txt', 'r')
#while True:
#    symbol = file.read(1)
#    if len(symbol) == 0:
#        break
#    print(symbol)

#file.close()

#file = open("pytonlessons/lesson20/test.txt", "w")
#file.writelines("Banana\n")
#file.writelines("Orange\n")
#file.close()

#file = open("pytonlessons/lesson20/test.txt")
#a = open("pytonlessons/lesson20/file.txt", "w")

#while True:
  #  symbol = file.read(1)
#    if len(symbol) == 0:
##        print("Whe end of the file")
 #       break
#    else:
#        a.write(f"{symbol}\n")
#a.close()
#file.close()
#===========
#a = open("pytonlessons/lesson20/file.txt", "w"):
with open("pytonlessons/lesson20/file.txt") as file:
    file.seek(2)
    print(file.read(1))