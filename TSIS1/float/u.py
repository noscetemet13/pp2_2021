a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
f=float(input())

if b!=0:
	y=(c*e-a*f)/(b*c-d*a)
	if c!=0:
		x=(f-d*y)/c
		print(str(x)+" "+str(y))
elif a!=0:
	x=(f*b-d*e)/(c*b-d*a)
	if d!=0:
		y=(f-c*x)/d
		print(str(x)+" "+str(y))