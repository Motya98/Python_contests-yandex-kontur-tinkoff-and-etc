vvod = [int(i) for i in input().split(' ')]
raskopok = vvod[1]
ukladok = vvod[2]
numbers_of_plitka = []
numbers_of_days = []
is_duplicater_or_not = {}
otvet = 0
for i in range(raskopok):
    j = input().split(' ')
    numbers_of_plitka.append(j[1])
    numbers_of_days.append(j[0])
    try:
        is_duplicater_or_not[j[1]] += 1
    except:
        is_duplicater_or_not[j[1]] = 1
uniq_plitok = len(set(numbers_of_plitka))
if uniq_plitok > ukladok:
    print(-1)
else:
    raznica_for_duplicates = ukladok - uniq_plitok
    for i in range(raskopok):
        if is_duplicater_or_not[numbers_of_plitka[i]] == 1:
            numbers_of_plitka[i] = 0
            numbers_of_days[i] = 0
        elif raznica_for_duplicates > 0:
            numbers_of_plitka[i] = 0
            numbers_of_days[i] = 0
            raznica_for_duplicates -= 1
        else:
            numbers_of_plitka[i] = int(numbers_of_plitka[i])
            numbers_of_days[i] = int(numbers_of_days[i])
    numbers_of_plitka_reverse = numbers_of_plitka.copy()
    numbers_of_plitka_reverse.reverse()
    otsev = [0]
    for plitka in range(raskopok):
        if numbers_of_plitka[plitka] not in otsev:
            index_plitka = numbers_of_plitka.index(numbers_of_plitka[plitka])
            index_plitka_OF = len(numbers_of_plitka) - numbers_of_plitka_reverse.index(numbers_of_plitka[plitka]) - 1
            otvet += numbers_of_days[index_plitka_OF] - numbers_of_days[index_plitka]
            otsev.append(numbers_of_plitka[plitka])
    print(otvet)


"""
5 4 3
1 2
2 3
2 1
6 2


2 4 2
1 1
1 2
3 1
4 2
"""
