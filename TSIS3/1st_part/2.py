a=list(map(int, input().split()))
b=[]
for i in a:
	if i>0:
		b.append(i)
print(min(b))