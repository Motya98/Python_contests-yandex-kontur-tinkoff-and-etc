vrem = [int(i) for i in input().split(' ')]
nominalov = vrem[1]
nominaly = [int(i) for i in input().split(' ')]
spisok_nominalov = []
for i in nominaly:
    for j in range(2):
        spisok_nominalov.append(i)
length = len(spisok_nominalov)
t = True
for i in range(length):
    su = vrem[0]
    chislo_kupyr_answer = 0
    kupyry_answer = []
    for j in range(i, length):
        su -= spisok_nominalov[j]
        chislo_kupyr_answer += 1
        kupyry_answer.append(str(spisok_nominalov[j]))
        if su == 0:
            print(chislo_kupyr_answer)
            vr = ' '.join(kupyry_answer)
            print(vr)
            t = False
            break
if t == True:
    for i in range(length):
        su = vrem[0]
        chislo_kupyr_answer = 0
        kupyry_answer = []
        for j in range(i, length):
            su -= spisok_nominalov[-j]
            chislo_kupyr_answer += 1
            kupyry_answer.append(str(spisok_nominalov[j]))
            if su == 0:
                print(chislo_kupyr_answer)
                vr = ' '.join(kupyry_answer)
                print(vr)
                t = False
                break

if t == True:
    print(-1)





"""
5 2
1 2

7 2
1 2

5 2
3 4
"""
