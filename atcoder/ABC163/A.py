import math
import sys
def getN():
    return int(input())

def getIntList():
    return list(map(int, input().split()))

def main():
    
    R = getN()

    print(2 * R * math.pi)


    return

if __name__ == "__main__":
    main()