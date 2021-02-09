cnt=0
a=-1
maxcnt=0
b=-1
while b!=0:
	b=int(input())
	if a==b:
		cnt+=1
	else:
		a=b
		maxcnt=max(maxcnt, cnt)
		cnt=1
print (maxcnt)