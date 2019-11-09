def chk(st):
    d = {}
    for i in st:
        d[i] = 1

    if len(d) != len(st):
        return False

    return True

n = int(input())
s = input()

if not chk(s):
    allnum = pow(2,n)-1

    d = {}
    for i in s:
        if i in d:
            d[i] = d[i]+1
        else:
            d[i] = 1

    minus = 0
    alld = 0
    f = 0
    for key in d.keys():
        if d[key] != 1:
            alld = alld+d[key]
            f=f+1
    #print(alld)

    for key in d.keys():
        if d[key] != 1:
            #print(pow(2,n-d[key]))
            #print(alld-d[key])
            minus = minus + (pow(2,n-d[key]))
            if f>1:
                minus = minus - (alld-d[key]-1)
    print(allnum-minus%(pow(10,9)+7))
else:
    print(pow(2,n)-1%(pow(10,9)+7))
