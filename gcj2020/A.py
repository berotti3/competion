T = int(input())


for num in range(T):
    N = int(input())

    #input square
    sq = []
    for i in range(N):
        sq.append(list(map(int,input().split())))

    #calc
    trace = 0
    for i in range(N):
        trace += sq[i][i]
    
    r = 0
    d = {}
    rsum = 0
    #check row
    for i in range(N):
        d = {}
        for j in range(N):
            #print(d)
            if sq[i][j] in d:
                r = i+1
                break
            else:
                d[sq[i][j]] = 1
        if r != 0:
            rsum += 1
            r = 0

    d = {}
    c = 0
    csum = 0
    #check col
    for i in range(N):
        
        d = {}
        for j in range(N):
            #print("i=" + str(i) + "j=" + str(j))
            #print(d)
            if sq[j][i] in d:
                #print("yes")
                c = i+1
                break
            else:
                d[sq[j][i]] = 1
        if c != 0:
            csum += 1
            c = 0
    
    print("Case #" + str(num+1) + ": " + str(trace) + " " + str(rsum) + " " + str(csum))