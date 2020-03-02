ABC=input().split()
A = int(ABC[0]);B = int(ABC[1]);C = int(ABC[2])


if (A < C and C < B) or (B < C and C < A):
    print("Yes")
else:
    print("No")
    

