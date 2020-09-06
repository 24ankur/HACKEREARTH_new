t=int(input())
for _ in range(t):
    n=int(input())
    s=0
    while n>=5:
        if n%5==0:
            r=n//5
            s=s+r
            n=r
        else:
            n=n-1

    print(s)

