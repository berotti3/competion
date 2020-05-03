def getN():
    return int(input())

def getIntList():
    return list(map(int, input().split()))


def main():

    N,K= map(int,input().split())

    slist = [0] * N

    for i in range(K):
        d = getN()
        A = getIntList()
        for j in range(d):
            slist[A[j]-1] += 1
    
    print(slist.count(0))
    
    return

if __name__ == "__main__":
    main()