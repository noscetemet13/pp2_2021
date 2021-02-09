def min4(a,b,c,d):
	mini=min(a,b)
	mini=min(mini,c)
	return(min(mini,d))
a=int(input())
b=int(input())
c=int(input())
d=int(input())
print(min4(a,b,c,d))