import math
import sys
def getN():
    return int(input())

# def gcd(p, q):
#     if p % q == 0: return q
#     return gcd(q, p % q)

def gcd(p, q):
    while q != 0:
        r = p % q
        p = q
        q = r
    return p

def main():
    
    K = getN()

    result = 0

    for i in range(1,K+1):
        for j in range(1,K+1):
            for k in range(1,K+1):
                result += gcd(gcd(i,j),k)
    
    print(result)

    return

if __name__ == "__main__":
    main()