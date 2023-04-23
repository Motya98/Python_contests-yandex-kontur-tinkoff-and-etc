kolvo_stran = int(input()) # число стран
dohod_stran = [int(i) for i in input().split(' ')] # минимальный необходимый доход
obrazovanie_stran = [int(i) for i in input().split(' ')] # нужно ли высшее образование для переезда
deti_stran = [int(i) for i in input().split(' ')] # могут ли дети переехать в страну без предыдущих условий
kolvo_karefanov = int(input()) # кол-во одноклассников
dohod_karefanov = [int(i) for i in input().split(' ')] # доход одноелассников
obrazovanie_karefanov = [int(i) for i in input().split(' ')] # образование одноклассников
deti_karefanov = [int(i) for i in input().split(' ')] # из какой станы их родители
spisok = []

for j in range(kolvo_karefanov): 
    for i in range(kolvo_stran): 
        if (dohod_karefanov[j] >= dohod_stran[i] and (obrazovanie_karefanov[j] == obrazovanie_stran[i] or obrazovanie_stran[i] == 0)) or (deti_stran[i] == 1 and deti_karefanov[j] == i + 1):
            spisok.insert(j, i + 1)
            break
    if len(spisok) < j + 1:
        spisok.insert(j, 0)
for i in spisok:
    print(i, end=' ')