T = int(input())


def devidefour(num: int):
    resultlist = []
    while num!=0:
        resultlist.append(num % 10)
        num = int(num/10)

    return resultlist


def makenum(numlist):
    result = 0

    for i in range(len(numlist)):
        result = result + numlist[i] * pow(10,i)

    return result


for n in range(T):
    N = int(input())

    numlist = devidefour(N)
    Anumlist = []
    Bnumlist = []

    for num in numlist:
        if num == 4:
            Anumlist.append(3)
            Bnumlist.append(1)
        else:
            Anumlist.append(num)
            Bnumlist.append(0)

    A = makenum(Anumlist)
    B = makenum(Bnumlist)
    
    print("Case #" + str(n+1) + ": " + str(A) + " " + str(B))