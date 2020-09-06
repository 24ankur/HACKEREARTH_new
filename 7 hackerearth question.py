import functools
import math
def Modulo(a, b) :
	mod = 0
	for i in range(0, len(b)) :
		mod = (mod * 10 + (int)(b[i])) % a

	return mod
def LastDigit(a, b) :
	len_a = len(a)
	len_b = len(b)
	if (len_a == 1 and len_b == 1 and b[0] == '0' and a[0] == '0') :
		return 1
	if (len_b == 1 and b[0]=='0') :
		return 1
	if (len_a == 1 and a[0] == '0') :
		return 0
	if((Modulo(4, b) == 0)) :
		exp = 4
	else :
		exp = Modulo(4, b)
	res = math.pow((int)(a[len_a - 1]), exp)
	return int(res) % 10

def fact(c):
    if c==1:
        return 1
    else:
        return c*fact(c-1)

a,b=map(str,input().split())
c=int(b)
if c<=5:

    ex=fact(c)
    y=str(ex%10)
    print(LastDigit(a, y))

else:
    print("1")


