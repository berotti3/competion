T = int(input())

def makeRRoute(RRoute):
    RRouteList = [['A']*N for i in range(N)]
    x = 0;y = 0;



for n in range(T):
    N = int(input())
    trials = 2*N-2
    RRoute = input()

    RRouteList = makeRRoute(RRoute)

    #simulate
    resultlist = ['A'] * trials

    if RRoute[0] == 'E':resultlist[0] = 'S';middlert = 'E'
    else:resultlist[0] = 'E';middlert = 'S'
    if RRoute[trials-1] == 'E':resultlist[trials-1] = 'S'
    else:resultlist[trials-1] = 'E'


    if resultlist[0] == 'E' and resultlist[trials-1] == 'S':
        resultlist = ['E']*(N-1) + ['S']*(N-1)
    elif resultlist[0] == 'S' and resultlist[trials-1] == 'E':
        resultlist = ['S']*(N-1) + ['E']*(N-1)
    else:
        firstrt = resultlist[0]

        count = 0;x=0;y=0
        for i in range(1,trials-1):

            if RRoute[i]==firstrt:x=x+1

            if RRoute[i] == firstrt:#magatta
                count = count+1
                if count == 2:
                    #print("x="+str(x))
                    resultlist = firstrt*(x-1) + middlert*(N-1) + firstrt*(N-x)
                    break
            else:count=0

    print("Case #" + str(n+1) + ": " + ''.join(resultlist))