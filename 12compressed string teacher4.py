import itertools


def compress(string):
    return ''.join(letter + str(len(list(group)))for letter, group in itertools.groupby(string))

if __name__ == '__main__':
    for i in range(int(input())):
        s=input()
        a=compress(s)
        print(a)
        if len(a)<len(s):
            print("YES")
        else:
            print("NO")
