n=int(input())
for _ in range(0,n):
    N,m=map(int,input().split())
    list1=list(map(int,input().split()))
    list2=list(map(int,input().split()))
    d={}
    for i in range (0,len(list1)):
        d.update({list1[i]:0})
    for j in range(len(list1)):
        d[list1[j]]=d[list1[j]]+list2[j]
    l=d.values()
    print(min(l))