import math

N = int(input())

cors = []
for i in range(N):

    xy = input().split()
    cors.append(xy)

sumnum = 0

n = 0
for i in range(N):

    for j in range(i,N):
        if i == j:
            continue
        else:
            n = n+1
            #print("i="+str(i) +"j="+str(j))
            xi = int(cors[i][0])
            xj = int(cors[j][0])
            yi = int(cors[i][1])
            yj = int(cors[j][1])
            sumnum = sumnum + math.sqrt((xj-xi)*(xj-xi)+(yj-yi)*(yj-yi))
print(sumnum/n*(N-1))
