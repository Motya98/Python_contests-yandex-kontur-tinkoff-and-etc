chislo_klavish = int(input()) 
nazv_klavish = [int(i) for i in input().split(' ')] 
ryad_klavish = [int(i) for i in input().split(' ')] 
chislo_v_referate = int(input()) 
symbols_of_referats = [int(i) for i in input().split(' ')]
porydok_ryadov = []
p = 0
otvet = 0
for j in symbols_of_referats:
    index_klavishi = nazv_klavish.index(j) 
    ryad = ryad_klavish[index_klavishi] 
    porydok_ryadov.append(ryad) 
    if p != 0:
        if porydok_ryadov[-2] != porydok_ryadov[-1]:
            otvet += 1
    p += 1
print(otvet)