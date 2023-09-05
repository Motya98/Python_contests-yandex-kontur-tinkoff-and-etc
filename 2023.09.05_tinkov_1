inp = [int(i) for i in input().split(' ')]
money = inp[1]
price_revolvers = [int(i) for i in input().split(' ')]
price_revolvers.append(money)
price_revolvers.sort()
index_money = price_revolvers.index(money)
try:
    if price_revolvers[index_money + 1] == money:
        print(money)
    elif price_revolvers[index_money + 1] != money:
        if index_money == 0:
            print(0)
        else:
            print(price_revolvers[index_money - 1])
except:
    print(price_revolvers[-2])
