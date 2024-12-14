import random

def shislo():
    get = random.randint(1, 100)
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуй угадать его!")

    while True:
            geer = int(input("Введите ваше предположение: "))
            
            if geer < get:
                print("НЕМНОГО больше.")
            elif geer > get:
                print("ПОЧТИ НО НЕМНОГО меньше.")
            else:
                print("НАКОНЕЦТО УГАДАЛ ЁМАЁ")
                break
shislo()
