spisok = [int(i) for i in input().split(' ')]
n = spisok[0] # строк
m = spisok[1] # столбцов
tablica = []
vse = []
stroka = None
stolbec = None
stroka_help = 0
stolbec_help = 0
s_stroka = 0
s_stolbec = 0
transp = []

for j in range(n):
    tablica.append([int(i) for i in input()])
    for k in tablica[-1]:
        vse.append(k)
max_vse = max(vse)  # максимальное значение из всех

for j in tablica:
    s_stroka += 1
    vrem_max = j.count(max_vse)  # подсчет максимального значения в каждой строке
    if vrem_max > stroka_help:
        stroka_help = vrem_max  # цифра максимально встречающегося максимального числа
        stroka = s_stroka  # строка с максимально встречающимся максимальным числом
tablica.pop(stroka - 1)  # удаляем строку с максимально часто встречающимся максимальным числом. s - 1, т.к. нумерация идет с 1
#print(tablica)

vse.clear()
for j in tablica:
    for i in j:
        vse.append(i)

max_vse = max(vse)  # новое максимальное значение
#print(vse)

for i in range(m):  # список для инкр повторяющихся значений в столбцах (заместо транспонирования)
    transp.append(0)

for j in tablica:
    for i in range(m):
        if j[i] == max_vse:
            transp[i] += 1
stolbec = transp.index(max(transp)) + 1 # отсчет от 1
print(stroka, stolbec)