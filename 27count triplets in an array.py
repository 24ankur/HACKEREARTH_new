from collections import Counter

def countTriplets(arr, r):
    result = 0
    dictOne = Counter()
    dictPairs = Counter()
    for i in reversed(arr):
        print(i)
        result += dictPairs[i*r]
        print("res",result)
        print(dictPairs)
        dictPairs[i] += dictOne[i*r]
        dictOne[i] += 1
        print(dictOne)
    return result



for _ in range(int(input())):
    arr=list(map(int,input().split()))
    r=int(input())
    print(countTriplets(arr,r))