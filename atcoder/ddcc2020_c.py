HWK = input().split()
H = int(HWK[0])
W = int(HWK[1])
K = int(HWK[2])

#input cake
cmap = []
for i in range(H):
    cmap.append(input())


#find cake
def findcake(x,y):
    for i in range(x,W):
        for j in range(y,H):
            if cmap[i][j]=="#":
                cmap[i][j] = "."
                return [i,j]
    return 0

def searchx(sty,cakey,cakex):
    for k in range(sty,cakey):#x
        for l in range(cakex+1,W):#y
            if cmap[k][l]=='#':
                return k-1
    return 0

def searchy(startx,cakey,stopx):

    for k in range(startx,stopx):
        for l in range(cakey+1,H):
            if cmap[k][l]=='#':
                return l-1
    return 0

def nuri(cake,startx,starty,stopx,stopy):
    ck = str(cake[0])+str(cake[1])

    for i in range(startx,stopx):
        for j in range(starty,stopy):
            cmap[i][j] = ck



for i in range(W):
    for j in range(H):
        start = [i, j]
        #find cake
        cake = findcake(i, j)
        stop = [0,0]
        #searchx
        stop[0] = searchx(start[1],cake[1],cake[0])

        #searchy
        stop[1] = searchy(start[0],cake[1],stop[0])

        #nuri
        nuri(cake,start[0],start[1],stop[0],stop[1])

        print(cmap)


print(cmap)


