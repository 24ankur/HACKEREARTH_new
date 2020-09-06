N=int(input())
s=input()
s=s.lower()

Q=int(input())
for _ in range(Q):
    x1,x2=map(int,input().split())
    print(s.count(max(s[x1:x2+1]), x1, x2 + 1))

