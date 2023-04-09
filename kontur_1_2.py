iterac = int(input())
perebor_prymoy = [int(element) for element in input().split(' ')]
perebor_obratniy = perebor_prymoy[::-1]
sprava = max(perebor_prymoy)
sleva = min(perebor_prymoy)

for i in perebor_obratniy:
    if i == sprava:
        sprava = iterac - perebor_obratniy.index(i)
        break

for i in perebor_prymoy:
    if i == sleva:
        sleva = perebor_prymoy.index(i) + 1
        break
print(sprava, sleva)