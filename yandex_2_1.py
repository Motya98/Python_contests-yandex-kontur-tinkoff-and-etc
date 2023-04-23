vvod = [int(i) for i in input().split(' ')]
n = vvod[0] # кол-во скульптур
x = vvod[1] # идеальное кол-во льда в скульптуре
t = vvod[2] # оставшееся кол-во минут
spisok = [int(i) for i in input().split(' ')] # кол-во льда в каждой скульптуре
otvet_kolvo = 0
otvet_index = []
convert = -1.0
nn = None

for i in range(n):
    max_spisok = max(spisok)
    for i in range(n):
        if type(spisok[i]) is not float:
            modul = abs(x - spisok[i])
            if modul < max_spisok:
                max_spisok = modul
                nn = i
    t = t - max_spisok
    if t < 0:
        break
    otvet_index.append((nn + 1))
    spisok[nn] = convert
    otvet_kolvo += 1
print(otvet_kolvo)
if len(otvet_index) != 0:
    for i in otvet_index:
        print(i, end=' ')