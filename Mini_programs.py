import os
import random

import Text
from calculator import calculator
from code_generator import graphic_code_generator
from common.input import проверка_ввода

k = 0
l = 5
вопрос = 2
spisok = 2

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
        spisok = graphic_code_generator.generator()
        p = 0

    while p == 3:
        spisok = calculator.calculator1()
        p = 0
os.system("pause")
