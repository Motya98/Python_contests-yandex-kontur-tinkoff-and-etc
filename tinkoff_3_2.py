n = int(input())
dengi = []
babki = input().split(' ')
for i in babki:
    dengi.append(int(i))
summa_1 = 0
otvet = []
for j in range(1, len(dengi)): # с заменой мест у 2 элементов
    summa = 0
    temp = dengi[j - 1]
    dengi[j - 1] = dengi[j]
    dengi[j] = temp
    for i in range(len(dengi)):
        if i == 0:
            summa += dengi[i]
        if i != 0 and i % 2 == 0:  # отписались
            summa += dengi[i]
        if i % 2 == 1:  # подписались
            summa -= dengi[i]
    otvet.append(summa)
    dengi = [] # наполняем список по новой
    for i in babki:
        dengi.append(int(i))

for i in range(len(dengi)): # проверка варианта без замены мест
    if i == 0:
        summa_1 += dengi[i]
    if i != 0 and i % 2 == 0:  # отписались
        summa_1 += dengi[i]
    if i % 2 == 1:  # подписались
        summa_1 -= dengi[i]
otvet.append(summa_1)
print(max(otvet))