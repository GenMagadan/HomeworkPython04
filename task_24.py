# В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сборана них выросло
# различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий
# модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном
# файле грядки.

from random import randint

bush = int(input("введите количество кустов: "))

berryes = []
for i in range(bush):
    berryes.append(randint(10, 30))
print(berryes)

gather = []
sum = 0
for i in range(len(berryes)):
    if (i == bush - 1):
        sum = berryes[i] + berryes[i - 1] + berryes[0]
    else:
        sum = berryes[i] + berryes[i - 1] + berryes[i + 1]
    gather.append(sum)
    gather.sort()
print(gather)
print(
    f"максимальное число за один заход: {gather[-1]} ягод")
