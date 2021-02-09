def IsPointInSquare(x, y):
	return(abs(x)<=1 and y==0 or x==0 and abs(y)<=1 or abs(x)<=0.5 and abs(y)<=0.5)
x=float(input())
y=float(input())
if IsPointInSquare(x, y):
	print('YES')
else:
	print('NO')