def getN():
    return int(input())

def getIntList():
    return list(map(int, input().split()))


def main():

    N,M= map(int,input().split())

    H = getIntList()

    # input AB
    ABlist = []
    for i in range(M):
        AB = list(map(int,input().split()))
        ABlist.append(AB)
    
    
    wlist = [1] * N
    for i in ABlist:
        if H[i[0]-1] < H[i[1]-1]:
            wlist[i[0]-1] = 0
        elif H[i[0]-1] == H[i[1]-1]:
            wlist[i[0]-1] = 0
            wlist[i[1]-1] = 0
        else:
            wlist[i[1]-1] = 0

    #print(wlist)
    print(wlist.count(1))

    return

if __name__ == "__main__":
    main()