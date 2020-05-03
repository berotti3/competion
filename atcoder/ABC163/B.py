

def getIntList():
    return list(map(int, input().split()))

def main():
    
    N,M = map(int,input().split())
    A = getIntList()

    for i in range(M):
        N -= A[i]
    
    if N >= 0:
        print(N)
    else:
        print(-1)

    return

if __name__ == "__main__":
    main()