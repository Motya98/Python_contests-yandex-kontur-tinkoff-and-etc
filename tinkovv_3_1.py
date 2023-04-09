dlina = int(input())
stroka = input()
otvet = []
for j in range(dlina + 1):
    for i in range(dlina + 1):
        stroka_itog = stroka[j:i:1]
        if 'a' in stroka_itog and 'b' in stroka_itog and 'c' in stroka_itog and 'd' in stroka_itog:
            otvet.append(len(stroka_itog))
if len(otvet) != 0:
    print(min(otvet))
else:
    print(-1)