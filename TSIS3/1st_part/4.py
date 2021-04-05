a=list(map(int, input().split()))
b=a.count(0)
for i in a:
	if i!=0:
		print(i, end=" ")
for i in range(b): print(0, end=" ")