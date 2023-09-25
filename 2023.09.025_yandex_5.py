slovar = {}
kolvo_of_abiturients = [int(i) for i in input().split(' ')][0]
budget_mesta = [int(i) for i in input().split(' ')]
for i in range(kolvo_of_abiturients):
    prioritets = []
    inp = [int(i) for i in input().split(' ')]
    for j in range(2, len(inp)):
        prioritets.append(inp[j])
    slovar[i] = inp[0], inp[1], prioritets
slovar = dict(sorted(slovar.items(), key=lambda i: i[1][0]))
for key, value in slovar.items():
    x = list(slovar[key])
    for position in range(value[2][0] - 1, value[2][-1]):
        if budget_mesta[position] != 0 and position + 1 in value[2]:
            x.append(position + 1)
            budget_mesta[position] -= 1
            slovar[key] = x
            break
        elif position == value[2][-1] - 1 and position + 1 in value[2]:
            x.append(-1)
            slovar[key] = x
slovar = dict(sorted(slovar.items()))
for value in slovar.values():
    print(value[-1], end=' ')


"""
4 2
1 5
3 1 1
1 1 2
2 2 1 2
3 2 1 2
"""
