import math


vvod = input()
vvod = vvod.split(' ')
n = int(vvod[0])
m = int(vvod[1])
k = int(vvod[2])
speed = m / k #число проверенных прог в единицу времени
otvet = math.ceil(n / speed)
print(otvet)