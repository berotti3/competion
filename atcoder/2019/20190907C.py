N = int(input())

B = [int(a) for a in input().split() ]

result = B[N-2]
old = B[N-2]
for i in range(N-3,-1,-1):
    #print(min(B[i],old))
    result = result + min(B[i],old)
    old  = B[i]


result = result + B[0]

print(result)


#0 0 10 10 10 23