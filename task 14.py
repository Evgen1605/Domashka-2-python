# Задача 14: Требуется вывести все целые степени двойки(т.е. числа вида 2 ^ k), не превосходящие числа N.

# Пример
# Ввод: 17 -> Вывод: 1, 2, 4, 8, 16

n = int(input('Введите число: '))
i = 0
while 2 ** i <= n:
    print(2 ** i)
    i +=1