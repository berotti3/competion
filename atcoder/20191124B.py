N = int(input())
S = input()

a_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = []
for i in S:
    num = a_list.index(i)
    result.append(a_list[(num+N)%26])

print(''.join(result))

