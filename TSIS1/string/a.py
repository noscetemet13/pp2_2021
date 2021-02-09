a=input()
print(a[2])
print(a[-2])
print(a[:5])
print(a[0:-2])
for i in range(len(a)):
	if i%2==0:
		print(a[i], end='')
print()
for i in range(len(a)):
	if i%2!=0:	
		print(a[i], end='')
print()
print(a[::-1])
for i in range(len(a)-1, -1, -2):
	print(a[i], end='')
print()
print(len(a))