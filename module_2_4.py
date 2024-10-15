def pass_gen():
    second_stone = []
    first_stone = int(input('Введите число с первого камня: '))
    while first_stone < 3 or first_stone > 20:
        first_stone = int(input("Неверно! Повторите ввод первого числа с камня:"))
    for i in range(1, first_stone):
        for k in range(i + 1, first_stone):
            if first_stone % (i + k) == 0:
                code = str(i) + str(k)
                second_stone.append(code)
    password_stone = ''
    for i in second_stone:
        password_stone += i
    print("Итоговый пароль: ", password_stone)

pass_gen()
