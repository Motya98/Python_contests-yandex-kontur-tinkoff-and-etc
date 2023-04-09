no_len = int(input())
ogr = 6 ** no_len
s = []
for i in range(no_len):
    s.append(0)
c = [-1]
otv = set()
ku = 1
no = [] # список списков
for j in range(no_len):
    no.append([int(i) for i in input().split()]) # если останется время, перебирать уникальные значения кубика через set
while ku != ogr:
    ku += 1
    m = 0
    h = 0
    for j in range(no_len):
        m += no[j][s[h]]
        h += 1
        if h == no_len:
            otv.add(m)
            m = 0
            h = 0
            s[-1] += 1
            for tr in c: # начало 1 блока. если, например, перебраны 2 кубика, и уже перебирается 3, то продолжаю итерировать 3.
                if s[tr] == 6 and s[-1] == 6:
                    s[tr - 1] += 1
                else:
                    break
            if s.count(6) == len(c): # 2 блок. если, например, перебраны 2 кубика полностью, то начинаю итерировать 3, обнуляя остальные.
                for yu in range(len(s)): # в случае срабоатывания этого блока не сработает конец 1 блока.
                    s[yu] = 0
                c.append(c[-1] - 1)
                s[c[-1]] += 1
            for tr in c: # конец 1 блока. если часть кубиков перебрана полностью, а один все еще нет, то обнуляем через этот блок (2 блок не срабатывает).
                if s[-1] == 6:
                    for tr in c:
                        if s[tr] == 6:
                            s[tr] = 0
                        else:
                            break
print(len(otv))