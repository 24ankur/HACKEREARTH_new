def theLoveLetterMystery(s):
    out = 0
    for i in range(len(s) // 2):
        out += abs(ord(s[i]) - ord(s[len(s) - i - 1]))
        print(ord(s[i]))
        print(ord(s[len(s) - i - 1]))

    return out
q = int(input())
for q_itr in range(q):
    s = input()

    result = theLoveLetterMystery(s)
    print(result)