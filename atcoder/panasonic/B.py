import math

HW = input().split()

H = int(HW[0])
W = int(HW[1])


result = int(0)

y1 = 0
y2 = 0
if W%2 == 1:
    y1 = int(W/2) + 1
    y2 = int(W/2)
else:
    y1 = int(W/2)
    y2 = y1


if H%2 == 1:
    result += y1 * (int(H/2) + 1)
    result += y2 * int(H/2)
else:
    result += y1 * int(H/2)
    result += y2 * int(H/2)

if H == 1 or W == 1:
    result = 1

print(result)

