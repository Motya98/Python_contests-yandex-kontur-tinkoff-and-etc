iterac = int(input())
gvozdi = []
gvozdi_copy = gvozdi.copy()
gvozdy_set = []
spisok_x = []
spisok_y = []
itog = []
for i in range(iterac):
    gvozdi.append([int(j) for j in input().split(' ')])
for i in gvozdi:
    spisok_x.append(i[0])
    spisok_y.append(i[1])
print(spisok_x)
print(spisok_y)
for i in range(iterac):
    if spisok_x.count(spisok_x[i]) > 1 and spisok_y.count(spisok_y[i]) > 1:
        gvozdy_set.append([spisok_x[i], spisok_y[i]])
for j in gvozdy_set:
    for i in gvozdy_set:
        for k in gvozdy_set:
            for z in gvozdy_set:
                if j[0] == i[0] and j[1] < i[1]:
                    if j[0] < k[0] and j[1] == k[1]:
                        b = (k[0] - j[0])
                        a = (i[1] - j[1])
                        print(a, b)
                        if a > 0 and b > 0:
                            if j[0] + b == z[0] and j[1] + a == z[1]:
                                itog.append(a * b)




if len(itog) != 0:
    print(f'otvet {max(itog)}')
else:
    print(0)