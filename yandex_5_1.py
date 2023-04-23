alfavit = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
vvod1 = [int(i) for i in input().split(' ')]
n = vvod1[0]
k = vvod1[1]
vvod2 = input()
text = []
for i in vvod2:
    text.append(i)
p = [int(i) for i in input().split(' ')]
d = [int(i) for i in input().split(' ')]
s = 0
s1 = 0
otvet = 0
otvet_set = {}
while n != 0:
    text_iterac = []
    text_iterac_istinniy = []
    tek_bukva = text[n - 1]
    for j in range(k):
        if text_iterac.count(tek_bukva) < 1:
            text_iterac.append(tek_bukva)
            otvet += len(set(text_iterac))
            text_iterac_istinniy.append(tek_bukva)
            if s == 0:
                position = p[n - 1]
                s += 1
            else:
                position = p[text.index(tek_bukva)]
            tek_bukva = text[position - 1]
        else:
            iterac = text_iterac_istinniy.count(tek_bukva) + 1
            nomer_v_alfavite = alfavit.index(tek_bukva)
            sdvig_pry_povtore = d[text.index(tek_bukva)]
            vrem = (nomer_v_alfavite + (iterac - 1) * sdvig_pry_povtore) % 26
            #print(nomer_v_alfavite, iterac, sdvig_pry_povtore, vrem)
            tek_bukva_vrem = alfavit[vrem]
            text_iterac.append(tek_bukva_vrem)
            otvet += len(set(text_iterac))
            text_iterac_istinniy.append(tek_bukva)
            position = p[text.index(tek_bukva)]
            tek_bukva = text[position - 1]
    n = n - 1
    #print(text_iterac)