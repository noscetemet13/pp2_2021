n=int(input())
a={}
for i in range(n):
	word, syn=input().split()
	a[word]=syn
	a[syn]=word
print(a[input()])