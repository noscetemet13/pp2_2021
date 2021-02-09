a=input()
space=a.find(' ')
print(a[(space+1):], end=' ')
print(a[:space])