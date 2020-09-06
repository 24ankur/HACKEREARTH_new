N,M=map(int,input().split())
arr=list(map(int,input().split()))[:N]
arr.sort()
x=[]
if N//M<M:
    print(sum(arr)%1000000007)

else:
    i=1
    while i<M:
        j=0
        while j<N:
            x.append(i*sum(arr[j:j+M]))
            j=j+M
            i=i+1
            if i==M:
                x.append(i*sum(arr[j:]))
                break



    print(sum(x)%1000000007)