number_of_reposit = int(input())
queues = [0]
incr_kolvo_max = 1
answer = 0

for i in range(number_of_reposit):
    queues.append(int(input()))
len_q = len(queues)
for i in range(len_q):
    incr_kolvo = 1
    ishodn_i = i
    while i != 0:
        i = queues[i]
        incr_kolvo += 1
    if incr_kolvo > incr_kolvo_max:
        incr_kolvo_max = incr_kolvo
        answer = ishodn_i
print(answer)
