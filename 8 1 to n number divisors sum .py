for _ in range(int(input())):
    n,k=map(int,input().split())
    l=[]
    for i in range(1,n+1):
        x=0
        for j in range(1,i+1):
            if i%j==0:
                res=j
                if res%k!=0:
                    x=max(res,x)
        l.append(x)
    print(l)
    print(sum(l))
