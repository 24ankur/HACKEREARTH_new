T=int(input())
for _ in range(T):
    N=int(input())
    arr=list(map(int,input().split()))
    c=1
    MAX=0
    MIN=N
    for i in range(N-1):
        if (arr[i+1]-arr[i])<=2:
            c=c+1


        else:
            MAX=max(MAX,c)
            MIN=min(MIN,c)
            c=1


    MAX=max(MAX,c)
    MIN=min(MIN,c)

    print(MAX)
    print(MIN)

