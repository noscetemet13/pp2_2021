a=int(input())
b=int(input())
c=int(input())
d=int(input())
x=abs(a-c)
y=abs(b-d)
if x==1 and y==2 or x==2 and y==1:
	print('YES')
else:
	print('NO')