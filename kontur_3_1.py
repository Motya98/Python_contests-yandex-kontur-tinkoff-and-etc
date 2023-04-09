itog = []
result = {}
iterac = int(input())
for i in range(iterac):
    y = input().split(' ')
    k = y[0]
    v = int(y[1])
    result[k] = v
y = input().split('-')
com_A = y[0]
com_B = y[1]
ochki = [3, 1, 0] #прибавляем к команде A
for i in ochki:
    result_temp = result.copy()
    result_temp[com_A] += i
    if i == 3:
        result_temp[com_B] += 0
    if i == 1:
        result_temp[com_B] += 1
    if i == 0:
        result_temp[com_B] += 3
    result_temp = dict(sorted(result_temp.items(), key=lambda item: item[1], reverse=True))
    #print(result_temp)
    nomer = 0
    for i in result_temp.keys():
        nomer += 1
        if i == com_A:
            print(nomer, end=' ')