import re

data = {}
y = int(input())
for i in range(y):
    t = input()
    v = re.findall('\d+', t)[0]
    k = t.split(f'{v}')[0]
    if k in data:
        data[k].append(int(v))
    else:
        data[k] = [int(v)]
u = []
y = int(input())
for i in range(y):
    t = input()
    u.append(t)
for street in u:
    if street not in data.keys():
        print(1)
        data[street] = 1
    else:
        for i in range(1, 300001):
            if i not in data[street]:
                print(i)
                data[street].append(i)
                break