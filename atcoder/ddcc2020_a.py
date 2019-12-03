
xy = input().split()
x = int(xy[0])
y = int(xy[1])

result = 0

if x == 1:
    result =result+ 300000
if y == 1:
    result =result+ 300000

if x == 2:
    result =result+ 200000
if y == 2:
    result =result+ 200000

if x == 3:
    result =result+ 100000
if y == 3:
    result =result+ 100000

if x == 1 and y==1:
    result =result+ 400000

print(result)