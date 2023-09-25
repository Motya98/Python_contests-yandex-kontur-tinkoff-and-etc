vvod = [int(i) for i in input().split(' ')]
vsego_dosok = vvod[0]
drop_dosok = vvod[1]
sizes = [int(i) for i in input().split(' ')]
sizes.sort()

for i in range(drop_dosok):
    avg = sum(sizes) / len(sizes)
    if sizes[-1] - avg >= avg - sizes[0]:
        sizes.pop()
    else:
        sizes.pop(0)
print(sizes[-1] - sizes[0])
