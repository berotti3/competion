T = int(input())


def findfour(num: int):
    while num!=0:
        if num % 10 == 4:
            return False
        else:
            num = int(num/10)
    return True


for n in range(T):
    N = int(input())

    for i in range(1,int(N/2)):

        if findfour(i):
            if findfour(N-i):
                print("Case #" + str(n+1) + ": " + str(i) + " " + str(N-i))
                break