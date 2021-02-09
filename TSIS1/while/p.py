cnt=0
a=-1
maxi=0
while a!=0:
	a=int(input())
	if a>maxi:
		maxi, cnt=a, 1
	elif a==maxi:
		cnt+=1
print (cnt)