import random

import Text


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


def generator():
    spisok = 2
    while True:
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
            if вопрос3 == 1:
                spisok = 1
            print(Text.прощание)
            print("    ")
            return spisok