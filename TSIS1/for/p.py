a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
cnt=0
for i in range(0, 1001):
	if i!=e:
		if ((a*(i**3)+b*(i**2)+c*i+d)/(i-e))==0:
			cnt+=1
print(cnt)