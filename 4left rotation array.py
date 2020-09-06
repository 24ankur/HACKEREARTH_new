from collections import deque
for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=deque(list(map(int,input().split())))
    arr.rotate(-k)
    arr=list(arr)
    print(*arr)