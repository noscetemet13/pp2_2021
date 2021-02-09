from math import sqrt
a=float(input())
b=float(input())
c=float(input())

d=b**2-4*a*c

if d>0:
	x1=(-b+sqrt(d))/(2*a)
	x2=(-b-sqrt(d))/(2*a)
	if(x1>x2):
		print(str(x2)+" "+str(x1))
	else:
		print(str(x1)+" "+str(x2))
elif d==0:
	x=(-b)/(2*a)
	print(x)
