T=int(input())
for i in range(T):
    N, K = map(int, input().split())
    arr= list(map(int, input().split()))
    G = 0
    T = 0
    R = 0
    L1 = []
    i = 0
    while i<=N-1:
        if arr[i]==i+1:
            i=i+1
        else:
            temp= arr[i]
            if arr[temp-1]==i+1:
                if G==0:
                    T=i+1
                    R=temp
                    arr[temp-1]=temp
                    G=1
                else:
                    L1.append([T,temp,R])
                    L1.append([i + 1,temp,R])
                    arr[temp- 1] =temp
                    G=0
                i=i+1
            else:
                Extra = arr[temp- 1]
                Extra_1= arr[Extra - 1]
                arr[i] =Extra_1
                arr[temp- 1] = temp
                arr[Extra - 1] = Extra
                L1.append([i+1,temp, Extra])

    if G==0 and len(L1)<=K:
        print(len(L1))
        for j in L1:
            print(*j)
    else:
        print("-1")