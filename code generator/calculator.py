import os

'''
							calculator
				  создан:  Максимилианом Савицким
				        При подержде python
'''
вопрос = 2
spisok = 2
p = 0


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


def calculator1():
    print("     ")
    a = int(input("ведите первое чило:"))
    print("     ")
    b = int(input("ведите второе число:"))
    print("     ")
    print("ведите число того действия что вы хотите сделать.")
    print("1 = плюс, 2 = минус, 3 = умножить, 4 = делить, 5 = следующая страница.")
    c = int(input())
    while c == 5 or c == 8:
        if c == 8:
            print("  ")
            print("первая страница")
            print("1 = плюс, 2 = минус, 3 = умножить, 4 = делить, 5 = следующая страница.")
        if c == 5:
            print("   ")
            print("2 стрн.")
            print("6 = степень, 7 = процент, 8 = первая страница.")
        c = int(input())
    if c == 1:
        d = int(input("хотите ли добавить ещё число к вашему действию? 0 - нет, 1 - да."))
        if d == 1:
            e = int(input("ведите третье число:"))
            print("ведите число того действия что вы хотите сделать.")
            print("1 = плюс, 2 = минус, 3 = умножить, 4 = делить, 5 = следующая страница.")
            g = int(input())
            while g == 5 or g == 8:
                if g == 8:
                    print("первая страница")
                    print("1 = плюс, 2 = минус, 3 = умножить, 4 = делить, 5 = следующая страница.")
                if g == 5:
                    print("2 стрн.")
                    print("6 = степень, 7 = процент, 8 = первая страница.")
                g = int(input())
            if g == 1:
                print("результат:", a + b + e)
            if g == 2:
                print("результат:", a + b - e)
            if g == 3:
                print("результат:", a + b * e)
            if g == 4:
                if b != 0 or e != 0:
                    print("результат:", a + b / e)
                else:
                    print("простите делить на ноль нельзя просим перезапустит программу.")
            if g == 6:
                print("результат:", a + b ^ e)
            if g == 7:
                if b != 0 or e != 0:
                    print("результат:", a + b % e)
                else:
                    print("простите остаток от деления на ноль невозможен просим перезапустит программу.")
        if d == 0:
            print("результат:", a + b)
    if c == 2:
        d = int(input("хотите ли добавить ещё число к вашему действию? 0 - нет, 1 - да."))
        if d == 1:
            e = int(input("ведите третье число:"))
            print("ведите число того действия что вы хотите сделать.")
            print("1 = плюс, 2 = минус, 3 = умножить, 4 = делить, 5 = следующая страница.")
            g = int(input())
            while g == 5 or g == 8:
                if g == 8:
                    print("первая страница")
                    print("1 = плюс, 2 = минус, 3 = умножить, 4 = делить, 5 = следующая страница.")
                if g == 5:
                    print("2 стрн.")
                    print("6 = степень, 7 = процент, 8 = первая страница.")
                g = int(input())
            if g == 1:
                print("результат:", a - b + e)
            if g == 2:
                print("результат:", a - b - e)
            if g == 3:
                print("результат:", a - b * e)
            if g == 4:
                if b != 0 or e != 0:
                    print("результат:", a - b / e)
                else:
                    print("простите делить на ноль нельзя просим перезапустит программу.")
            if g == 6:
                print("результат:", a - b ^ e)
            if g == 7:
                if b != 0 or e != 0:
                    print("результат:", a - b % e)
                else:
                    print("простите остаток от деления на ноль невозможен просим перезапустит программу.")
        if d == 0:
            print("результат:", a - b)
    if c == 3:
        d = int(input("хотите ли добавить ещё число к вашему действию? 0 - нет, 1 - да."))
        if d == 1:
            e = int(input("ведите третье число:"))
            print("ведите число того действия что вы хотите сделать.")
            print("1 = плюс, 2 = минус, 3 = умножить, 4 = делить, 5 = следующая страница.")
            g = int(input())
            while g == 5 or g == 8:
                if g == 8:
                    print("первая страница")
                    print("1 = плюс, 2 = минус, 3 = умножить, 4 = делить, 5 = следующая страница.")
                if g == 5:
                    print("2 стрн.")
                    print("6 = степень, 7 = процент, 8 = первая страница.")
                g = int(input())
            if g == 1:
                print("результат:", a * b + e)
            if g == 2:
                print("результат:", a * b - e)
            if g == 3:
                print("результат:", a * b * e)
            if g == 4:
                if b != 0 or e != 0:
                    print("результат:", a * b / e)
                else:
                    print("простите делить на ноль нельзя просим перезапустит программу.")
            if g == 6:
                print("результат:", a * b ^ e)
            if g == 7:
                if b != 0 or e != 0:
                    print("результат:", a * b % e)
                else:
                    print("простите остаток от деления на ноль невозможен просим перезапустит программу.")
        if d == 0:
            print("результат:", a * b)
    if c == 4:
        d = int(input("хотите ли добавить ещё число к вашему действию? 0 - нет, 1 - да."))
        if d == 1:
            e = int(input("ведите третье число:"))
            print("ведите число того действия что вы хотите сделать.")
            print("1 = плюс, 2 = минус, 3 = умножить, 4 = делить, 5 = следующая страница.")
            g = int(input())
            while g == 5 or g == 8:
                if g == 8:
                    print("первая страница")
                    print("1 = плюс, 2 = минус, 3 = умножить, 4 = делить, 5 = следующая страница.")
                if g == 5:
                    print("2 стрн.")
                    print("6 = степень, 7 = процент, 8 = первая страница.")
                g = int(input())
            if g == 1:
                print("результат:", a / b + e)
            if g == 2:
                print("результат:", a / b - e)
            if g == 3:
                print("результат:", a / b * e)
            if g == 4:
                if b != 0 or e != 0:
                    print("результат:", a / b / e)
                else:
                    print("простите делить на ноль нельзя просим перезапустит программу.")
            if g == 6:
                print("результат:", a / b ^ e)
            if g == 7:
                if b != 0 or e != 0:
                    print("результат:", a / b % e)
                else:
                    print("простите остаток от деления на ноль невозможен просим перезапустит программу.")
        if d == 0:
            if b != 0:
                print("результат:", a / b)
            else:
                print("простите делить на ноль нельзя просим перезапустит программу.")
    if c == 6:
        d = int(input("хотите ли добавить ещё число к вашему действию? 0 - нет, 1 - да."))
        if d == 1:
            e = int(input("ведите третье число:"))
            print("ведите число того действия что вы хотите сделать.")
            print("1 = плюс, 2 = минус, 3 = умножить, 4 = делить, 5 = следующая страница.")
            g = int(input())
            while g == 5 or g == 8:
                if g == 8:
                    print("первая страница")
                    print("1 = плюс, 2 = минус, 3 = умножить, 4 = делить, 5 = следующая страница.")
                if g == 5:
                    print("2 стрн.")
                    print("6 = степень, 7 = процент, 8 = первая страница.")
                g = int(input())
            if g == 1:
                print("результат:", a ** b + e)
            if g == 2:
                print("результат:", a ** b - e)
            if g == 3:
                print("результат:", a ** b * e)
            if g == 4:
                if b != 0 or e != 0:
                    print("результат:", a ** b / e)
                else:
                    print("простите делить на ноль нельзя просим перезапустит программу.")
            if g == 6:
                print("результат:", a ** b ^ e)
            if g == 7:
                if b != 0 or e != 0:
                    print("результат:", a ** b % e)
                else:
                    print("простите остаток от деления на ноль невозможен просим перезапустит программу.")
        if d == 0:
            print("результат:", a ** b)
    if c == 7:
        d = int(input("хотите ли добwавить ещё число к вашему действию? 0 - нет, 1 - да."))
        if d == 1:
            e = int(input("ведите третье число:"))
            print("ведите число того действия что вы хотите сделать.")
            print("1 = плюс, 2 = минус, 3 = умножить, 4 = делить, 5 = следующая страница.")
            g = int(input())
            while g == 5 or g == 8:
                if g == 8:
                    print("первая страница")
                    print("1 = плюс, 2 = минус, 3 = умножить, 4 = делить, 5 = следующая страница.")
                if g == 5:
                    print("2 стрн.")
                    print("6 = степень, 7 = процент, 8 = первая страница.")
                g = int(input())
            if g == 1:
                print("результат:", a % b + e)
            if g == 2:
                print("результат:", a % b - e)
            if g == 3:
                print("результат:", a % b * e)
            if g == 4:
                if b != 0 or e != 0:
                    print("результат:", a % b / e)
                else:
                    print("простите делить на ноль нельзя просим перезапустит программу.")
            if g == 6:
                print("результат:", a % b ^ e)
            if g == 7:
                if b != 0 or e != 0:
                    print("результат:", a % b % e)
                else:
                    print("простите остаток от деления на ноль невозможен просим перезапустит программу.")
        if d == 0:
            if b != 0:
                print("результат:", a % b)
            else:
                print("простите остаток от деления на ноль невозможен просим перезапустит программу.")
    print("     ")
    print("Спасибо за использование нашего калькулятора")
    print("версия калькулятора 3.0")
    print("     ")
    print("Хотите ли вы начать заного?")
    print("     ")
    вопрос5 = проверка_ввода(0, 1, "0 - нет, 1 - да.")
    if вопрос5 == 0:
        print("Хотите ли вернутся к списку программ?")
        вопрос6 = проверка_ввода(0, 1, "0 - нет, 1 - да.")
        if вопрос6 == 0:
            spisok = 0
            p = 0
        if вопрос6 == 1:
            spisok = 1
            p = 0


os.system("pause")
