from sys import stdin
a=(str(stdin.read()).split())
b={}
for i in a:
	b[i]=b.get(i, 0)+1
b=[(x, y) for y, x in b.items()]
b.sort(key=lambda x:(-x[0],x[1]))
for i in range(len(b)):
	print(b[i][1])