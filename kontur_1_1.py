x = input()
y = []
for i in x:
    y.append(int(i))
y1 = sorted(y)
y2 = y1[::-1]

y11 = []
y22 = []
for i in y1:
    y11.append(str(i))
for i in y2:
    y22.append(str(i))
y11 = int(''.join(y11))
y22 = int(''.join(y22))
print(y22 - y11)