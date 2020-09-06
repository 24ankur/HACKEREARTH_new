N = int(input())
M = []
w=[]
for i in range(N):
    x =input().split()
    if x[1].endswith("@gmail.com"):
        M.append(x[0])

M.sort()
for i in M:
    print(i)