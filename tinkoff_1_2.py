perviy = input().split(' ')
x1_perviy = int(perviy[0])
y1_perviy = int(perviy[1])
x2_perviy = int(perviy[2])
y2_perviy = int(perviy[3])

vtoroy = input().split(' ')
x1_vtoroy = int(vtoroy[0])
y1_vtoroy = int(vtoroy[1])
x2_vtoroy = int(vtoroy[2])
y2_vtoroy = int(vtoroy[3])

if x2_perviy > x2_vtoroy and y1_perviy < y1_vtoroy:
    ab = x2_perviy - x1_vtoroy
    bc = y2_vtoroy - y1_perviy
    if ab == bc:
        print(ab * bc)
    if ab != bc:
        extremium = max([ab, bc])
        print(extremium  2)
if x2_perviy > x2_vtoroy and y1_perviy > y1_vtoroy:
    ab = x2_perviy - x1_vtoroy
    bc = y2_perviy - y1_vtoroy
    if ab == bc:
        print(ab * bc)
    if ab != bc:
        extremium = max([ab, bc])
        print(extremium  2)
if x1_perviy < x1_vtoroy and y1_perviy > y1_vtoroy:
    ab = x2_vtoroy - x1_perviy
    bc = y2_perviy - y1_vtoroy
    if ab == bc:
        print(ab * bc)
    if ab != bc:
        extremium = max([ab, bc])
        print(extremium  2)
if x1_perviy < x1_vtoroy and y1_perviy < y1_vtoroy:
    ab = x2_vtoroy - x1_perviy
    bc = y2_vtoroy - y1_perviy
    if ab == bc:
        print(ab * bc)
    if ab != bc:
        extremium = max([ab, bc])
        print(extremium  2)