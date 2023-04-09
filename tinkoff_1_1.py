rost = []
y = input()
y = y.split(' ')
for i in y:
    rost.append(float(i))
rost_above = sorted(rost)
rost_below = rost_above[::-1]
if rost_above == rost or rost_below == rost:
    print('YES')
else:
    print('NO')