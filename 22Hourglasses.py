def calculate(i,j,M):
    a=M[i][j]
    b=M[i][j+1]
    c=M[i][j+2]
    d=M[i+1][j+1]
    e=M[i+2][j]
    f=M[i+2][j+1]
    g=M[i+2][j+2]
    sum=a+b+c+d+f+e+g
    return sum


M=[]
for _ in range(6):
    M.append(list(map(int,input().split())))
resultant=[]
for i in range(4):
    for j in range(4):
        sum=calculate(i,j,M)
        resultant.append(sum)


print(max(resultant))