a=int(input())
b=int(input())

for i in range(a, b+1):
	rev=0
	n=i
	while(n>0):
		ld=n%10
		rev=rev*10+ld
		n=n//10
	if(i==rev):
		print(i)