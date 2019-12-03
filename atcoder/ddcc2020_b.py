
N = int(input())
A = list(map(int, input().split()))

sums =sum(A)

l = 0
mlen = sums
for i in A:
    l += i
    r = sums - l
    #print("l="+str(l) + "r="+str(r))

    lr =l-r
    if lr <0:lr*=-1

    #print("mlen="+str(mlen)+"rl=" + str(lr))
    if mlen < lr:
        break
    else:
        mlen = r-l
        if mlen <0:mlen*=-1



print(mlen)