X = int(input())

result = 0

result += int(X/500) * 1000
X -= int(X/500) * 500

result += int(X/5) * 5

print(result)