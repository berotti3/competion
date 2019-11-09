import collections
N = int(input())

D = [int(a) for a in input().split() ]

counted = collections.Counter(D)

if D[0] != 0 or counted[0] !=1:
    print("0")
    exit()

#calc
result = 1
x = counted[1]
for i in range(2,N+1):
    y = counted[i]
    result = result * pow(x,y) %998244353
    x = y
print(result)
