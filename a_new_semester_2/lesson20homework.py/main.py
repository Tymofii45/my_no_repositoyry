#Створити програму, яка запитує імена користувачів, та дозаписує їх у файл, 
#допоки користувач не введе "q" (цикл обривається)
while True:
    a = input("Hi!Please print something: ")
    if a != "q":
        file = open('pytonlessons/lesson20homework/text.txt', 'w')
        file.write(a)
        file.close()
        print("Sent-successfully!")
    else:
        print("Work ended!")
        break

    