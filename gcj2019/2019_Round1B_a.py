T = int(input())

for n in range(T):
    P,Q = map(int,input().split())

    maps = [[0]*(Q) for i in range(Q)]

    for m in range(P):
        XYD = input().split()
        X = int(XYD[0]);Y = int(XYD[1]);D = XYD[2]

        minX = 0;minY = 0
        maxX = Q-1;maxY = Q-1
        if D == "N":
            minY = Y+1
        elif D == "E":
            minX = X+1
        elif D == "S":
            maxY = Y-1
        else:
            maxX = X-1
        for i in range(minX,maxX+1):
            for j in range(minY,maxY+1):
                maps[i][j] = maps[i][j]+1

    resultj = 0;resulti = 0;
    maxpoint = 0
    for i in range(Q-1,-1,-1):
        for j in range(Q-1,-1,-1):
            if maxpoint<=maps[i][j]:
                resultj = j;resulti = i
                maxpoint = maps[i][j]

    print("Case #" + str(n+1) + ": " + str(resulti) + " " + str(resultj))

