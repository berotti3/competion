N = int(input())

dic = {}

for i in range(N):
	key = input()
	if key not in dic:
		dic[key] = 1
	else:
		dic[key] +=1

maxnum = max(dic.values())
#print(maxnum)
#print(dic)

keys = list(dic.keys())
for key in sorted(keys):
	if dic[key] == maxnum:
		print(key)


