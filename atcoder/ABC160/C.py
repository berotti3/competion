K,N = map(int,input().split())

A = list(map(int,input().split()))

point = A[0]
maxlen = A[0] + (K-A[N-1])
for i in range(1,N):
    maxlen = max(A[i]-A[i-1],maxlen)
    #print(str(A[i]-A[i-1]) + "max="+str(maxlen))


print(K-maxlen)
