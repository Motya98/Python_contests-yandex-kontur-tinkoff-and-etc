inp = input()
spisok = 'sherif'
f = 0
slovar_not_double = {}
for i in inp:
    if i in spisok:
        try:
            if i != 'f':
                incr = slovar_not_double[i]
                incr += 1
                slovar_not_double[i] = incr
            else:
                f += 1
                incr = slovar_not_double[i]
                if f == 2:
                    f -= 2
                    incr += 1
                    slovar_not_double[i] = incr
        except:
            if i != 'f':
                slovar_not_double[i] = 1
            else:
                f += 1
                if f == 2:
                    f -= 2
                    incr = 1
                    slovar_not_double[i] = incr
if len(slovar_not_double) == 6:
    print(slovar_not_double[min(slovar_not_double)])
else:
    print(0)


# fheriherffazfszkisrrs
# rifftratatashe
# thegorillaiswatching
