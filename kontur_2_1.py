y = int(input())
m = []
for i in range(y):
    m.append(int(input()))
z = []
while True:
    if len(m) == 1:
        print(-m[0])
        break
    for j in m:
        for i in m:
            if j + i == 0:
                z.append(j)
                z.append(i)
                m.remove(j)
                m.remove(i)
