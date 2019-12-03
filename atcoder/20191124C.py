ABX = input().split()
A = int(ABX[0])
B = int(ABX[1])
X = int(ABX[2])

def calc(N):
    return A*N + B*len(str(N))


maxN = 0
result = 0


for N in range(min(int((X-B*10)/A)-1,pow(10,9)),min(int((X)/A)+1,pow(10,9)+1)):
    #print(N)
    c = calc(N)
    #print("maxN="+str(maxN)+"c="+str(c))
    if c < X:
        if maxN<c:
            maxN = c
            result = N

print(result)



