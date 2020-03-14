import math

ABC = input().split()

a = int(ABC[0])
b = int(ABC[1])
c = int(ABC[2])
#a = b = c = pow(10,9)

l2  = 4 * a * b
r = c - a - b
r2 = r * r

# if l2 < r2:
#     print("Yes")
# else:
#     print("No")

if r > 0 :
    if l2 < r2:
        print("Yes")
    else:
        print("No")
else:
    print("No")


