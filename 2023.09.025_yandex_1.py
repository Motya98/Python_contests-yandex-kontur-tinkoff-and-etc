usb_in_pc = int(input())
usb_need = int(input())
price_c_2 = int(input())
price_c_5 = int(input())
solves = []
money = 0
usb_different = usb_need - usb_in_pc

avg_c_2 = price_c_2 / 2
avg_c_5 = price_c_5 / 5

if avg_c_2 <= avg_c_5:
    while usb_different > 0:
        usb_different -= 1
        money += price_c_2
    print(money)
else:
    while usb_different > 0:
        usb_different -= 4
        money += price_c_5
    solves.append(money)
    usb_different += 4
    money -= price_c_5
    while usb_different > 0:
        usb_different -= 1
        money += price_c_2
    solves.append(money)
    print(min(solves))
