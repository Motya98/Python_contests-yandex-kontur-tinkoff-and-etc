teams = int(input())
otbor = []
otvet = []
for i in range(teams):
    t = sorted(input().split(' '))
    otbor.append(t)
for j in range(teams):
    s = 0
    for i in range(teams):
        if otbor[j] == otbor[i]:
            s += 1
    otvet.append(s)
print(max(otvet))