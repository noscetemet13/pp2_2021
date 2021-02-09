n=int(input())
sum=float(0)
for i in range(n+1):
	if(i%2==1):
		sum+=(-1)/(2*i+1)
	else:
		sum+=1/(2*i+1)
print(4*sum)