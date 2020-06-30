import os
import Text
import random
import calculator
k = 0
l = 5
вопрос = 2
spisok = 2


def проверка_ввода(min, max, сообщение):
    while True:
        vodd = input(сообщение)
        try:
            vodd = int(vodd)
            if vodd > max or vodd < min:
                print("нет такой значения")
            else:
                return vodd
        except:
            print("нужно конктретно число")


print("Приветствую! Моё имя Максимилиан Савицкий и я создатель этих программ прошу выбрать программу.")
print("выбор производится написагием нужной цыфры.")
while spisok == 2 or spisok == 1:
    if spisok == 1:
        print("         ")
        print("Список программ:")
        spisok = 2
    if spisok == 2:
        print("1. /\\/Мини игра угадай число/\\/")
        print("2. #|Генератор случайных графических паролей|#")
        print("3. 2+2 Калькулятор 1+2")
    p = проверка_ввода(1, 3, "ведите номер программы: ")
    b = 1
    while p == 1:
        if вопрос == 2:
            print(Text.text1)
        if вопрос == 1:
            c = 0
            k = 0
            l = 5
            print(Text.text0)
        c = int(input("напишите номер уровня сложности:"))
        if c == 1:
            k = 26
        if c == 2:
            k = 51
            l *= 2
        if c == 3:
            k = 101
            l = l * 2
        number = random.randint(1, k)
        print("   ")
        while l != 0:
            s = int(input("напишите число которое по вашему мнению загадал компьютер:"))
            if number != s:
                l = l - 1
                print("неправильно")
                print("  ")
                if number > s:
                    print("подзказка:твоё число меньше чем число загаданое компьютером")
                    print("  ")
                if number < s:
                    print("подзказка:твоё число больше чем число загаданое компьютером.")
                    print("  ")
                print('попыток осталось', l)
            if number == s:
                print("  ")
                print("победа!")
                l = 0
        print("  ")
        print("Игра завершена")
        print("  ")
        print("Хотите ли повторить игру?")
        вопрос = проверка_ввода(0, 1, "0 - нет, 1 - да.")
        if вопрос == 0:
            print("Хотите ли вернутся к списку программ?")
            вопрос2 = проверка_ввода(0, 1, "0 - нет, 1 - да.")
            if вопрос2 == 0:
                spisok = 0
                p = 0
            if вопрос2 == 1:
                spisok = 1
                p = 0
    while p == 2:
        print("Какой длины генерировать пароль?")
        print("    ")
        print("Мин. длина 5, Макс. длина. 9.")
        dlina = проверка_ввода(5, 9, "")
        print("    ")
        Code1 = random.randint(1, 9)
        Code2 = random.randint(1, 9)
        while Code1 == Code2:
            Code2 = random.randint(1, 9)
        Code3 = random.randint(1, 9)
        while Code1 == Code3 or Code2 == Code3:
            Code3 = random.randint(1, 9)
        Code4 = random.randint(1, 9)
        while Code1 == Code4 or Code2 == Code4 or Code3 == Code4:
            Code4 = random.randint(1, 9)
        Code5 = random.randint(1, 9)
        while Code1 == Code5 or Code2 == Code5 or Code3 == Code5 or Code4 == Code5:
            Code5 = random.randint(1, 9)
        if dlina == 6 or dlina == 7 or dlina == 8 or dlina == 9:
            Code6 = random.randint(1, 9)
            while Code1 == Code6 or Code2 == Code6 or Code3 == Code6 or Code4 == Code6 or Code5 == Code6:
                Code6 = random.randint(1, 9)
            if dlina == 7 or dlina == 8 or dlina == 9:
                Code7 = random.randint(1, 9)
                while Code1 == Code7 or Code2 == Code7 or Code3 == Code7 or Code4 == Code7 or Code5 == Code7 or Code6 == Code7:
                    Code7 = random.randint(1, 9)
                if dlina == 8 or dlina == 9:
                    Code8 = random.randint(1, 9)
                    while Code1 == Code8 or Code2 == Code8 or Code3 == Code8 or Code4 == Code8 or Code5 == Code8 or Code6 == Code8 or Code7 == Code8:
                        Code8 = random.randint(1, 9)
                    if dlina == 9:
                        Code9 = random.randint(1, 9)
                        while Code1 == Code9 or Code2 == Code9 or Code3 == Code9 or Code4 == Code9 or Code5 == Code9 or Code6 == Code9 or Code7 == Code9 or Code8 == Code9:
                            Code9 = random.randint(1, 9)
        if dlina == 9:
            print(Code1, ">", Code2, ">", Code3, ">", Code4, ">", Code5, ">", Code6, ">", Code7, ">", Code8, ">", Code9)
        if dlina == 8:
            print(Code1, ">", Code2, ">", Code3, ">", Code4, ">", Code5, ">", Code6, ">", Code7, ">", Code8)
        if dlina == 7:
            print(Code1, ">", Code2, ">", Code3, ">", Code4, ">", Code5, ">", Code6, ">", Code7)
        if dlina == 6:
            print(Code1, ">", Code2, ">", Code3, ">", Code4, ">", Code5, ">", Code6)
        if dlina == 5:
            print(Code1, ">", Code2, ">", Code3, ">", Code4, ">", Code5)
        print("Сгенерировать другой пароль?")
        вопрос4 = проверка_ввода(0, 1, "0 - нет, 1 - да.")
        if вопрос4 == 0:
            print("Хотите ли вернутся к списку программ?")
            вопрос3 = проверка_ввода(0, 1, "0 - нет, 1 - да.")
            if вопрос3 == 0:
                spisok = 0
                p = 0
            if вопрос3 == 1:
                spisok = 1
                p = 0
            print(Text.прощание)
            print("    ")

    while p == 3:
         calculator.calculator1()
os.system("pause")
