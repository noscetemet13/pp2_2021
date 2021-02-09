a=input()
i=a.find('f')
if i!=-1:
	j=a.rfind('f', i+1, len(a))
	if j!=-1:
		print(i, j)
	else:
		print(i)