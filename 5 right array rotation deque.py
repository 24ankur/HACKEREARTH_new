from collections import deque
for _ in range(int(input())):
    l,b = map(int,input().split())
    a = deque(list(map(int,input().split())))
    a.rotate(b)
    a = list(a)
    print(" ".join(str(e) for e in a))