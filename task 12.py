# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел s и их произведение p. Помогите Кате отгадать задуманные Петей числа.

# Пример
# Ввод: 5 6 -> Вывод: 2 3

# numberX = int(input('Введите число X: '))
# numberY= int(input('Введите число Y: '))

# for i in range(numberX):
#   for j in range(numberY):
#     if numberX == i + j and numberY == i * j:
#       print(i, j)

# Решаем по формуле  Виета
s = int(input('Сумма: '))
p = int(input('Произведение: '))

x = (s + (s**2 - 4*p)**(0.5)) / 2
y = (s - (s**2 - 4*p)**(0.5)) / 2
print(x, y)