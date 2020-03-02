N = int(input())

A = [int(a) for a in input().split() ]
B = [int(a) for a in input().split() ]
C = [int(a) for a in input().split() ]

result = 0
old = -5
for i in range(N):#foodA[i]
    result = result + B[A[i]-1]

    if (A[i]-2 == old):
        result = result + C[old]

    old  = A[i]-1
    #print(result)

print(result)
