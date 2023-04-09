p = [int(i) for i in input().split(' ')]
N = p[0]
K = p[1]
s = 0
spisok = [int(i) for i in input().split(' ')]
for j in range(N):
    iterac_o = 0
    s_vrem = spisok[j]
    if s_vrem <= K:
        s += 1
        if s_vrem == 0:
            iterac_o += 1
    else:
        continue
    for i in range(j + 1, N):
        s_vrem += spisok[i]
        if spisok[i] == 0:
            iterac_o += 1
            if iterac_o > 1:
                break
        if s_vrem <= K:
            s += 1
        else:
            break
print(s)