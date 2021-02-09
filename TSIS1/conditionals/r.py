N=int(input())
M=int(input())
x=int(input())
y=int(input())
if N>M:
	temp=M
	M=N
	N=temp
if x>=N/2:
	x=N-x
if y>=M/2:
	y=M-y
if x>y:
	print(y)
else:
	print(x)