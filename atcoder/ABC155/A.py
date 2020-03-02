
ABC = input().split()

A = ABC[0]
B = ABC[1]
C = ABC[2]

if A==B:
	if B==C:
		print("No")
	else:
		print("Yes")
	exit()

if B==C:
	if A==C:
		print("No")
	else:
		print("Yes")
	exit()

if A==C:
	if B==C:
		print("No")
	else:
		print("Yes")
	exit()

print("No")	
