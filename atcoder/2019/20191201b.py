import math
N = int(input())

X = math.ceil(N/1.08)



if N == int(X*1.08):
    print(int(X))
else:
    #print(int(X))
    print(":(")

