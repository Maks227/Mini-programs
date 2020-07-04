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