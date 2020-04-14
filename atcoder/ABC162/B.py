import math
import sys
def getN():
    return int(input())

def getIntList():
    return list(map(int, input().split()))

def main():
    
    N = getN()

    result = 0
    for i in range(1,N+1):
        if i % 5 != 0 and i % 3 != 0:
            result += i
            #print(i)
    
    print(result)

    return

if __name__ == "__main__":
    main()