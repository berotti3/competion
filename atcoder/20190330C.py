NQ = input().split()
N = int(NQ[0])
Q = int(NQ[1])
words = input() #s

num_golem = [1]*N

for i in range(Q):#simulate
    td = input().split()
    tword = td[0]
    direction = td[1]

    for j in range(N):
        if words[j] == tword:
            if direction == 'L' and not j==0:
                num_golem[j-1] = num_golem[j-1] + num_golem[j]
            elif direction == 'R' and not j==N-1:
                num_golem[j+1] = num_golem[j+1] + num_golem[j]
            num_golem[j] = 0

print(sum(num_golem))