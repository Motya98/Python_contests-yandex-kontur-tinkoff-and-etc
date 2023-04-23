n = int(input()) # число дней
prices = [int(i) for i in input().split(' ')]
spisok_1 = []
spisok_2 = []
koordinaty_1 = []
koordinaty_2 = []

for j in range(n): 
    s_pokupki = 1 / prices[j]
    for i in range(j + 1, n, 1):
        s_prodagi = round(s_pokupki * prices[i], 5)
        spisok_1.append(s_prodagi)
        koordinaty_1.append((j + 1, i + 1)) 
luchee_1 = max(spisok_1)
days_1 = koordinaty_1[spisok_1.index(luchee_1)]


if n >= 4:
    for j in range(n):
        s_pokupki_1 = 1 / prices[j]
        for i in range(j + 1, n, 1):
            s_prodagi_1 = s_pokupki_1 * prices[i]
            for jj in range(i + 1, n, 1):
                s_pokupki_2 = s_prodagi_1 / prices[jj]
                for ii in range(jj + 1, n, 1):
                    s_prodagi_2 = s_pokupki_2 * prices[ii]
                    spisok_2.append(s_prodagi_2)
                    koordinaty_2.append((j + 1, i + 1, jj + 1, ii + 1))
if len(spisok_2) == 0: 
    spisok_2.append(-1)
    koordinaty_2.append((0, 0))
luchee_2 = max(spisok_2)
days_2 = koordinaty_2[spisok_2.index(luchee_2)]

if luchee_1 > luchee_2 and luchee_1 > 1:
    print(1)
    print(days_1[0], days_1[1])
if luchee_2 >= luchee_1 and luchee_2 > 1:
    print(2)
    print(days_2[0], days_2[1])
    print(days_2[2], days_2[3])
if luchee_1 <= 1 and luchee_2 <= 1:
    print(0)