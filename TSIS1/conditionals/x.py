a=int(input())
b=int(input())
c=int(input())
x=int(input())
y=int(input())
z=int(input())

v1=(a//x)*(b//y)*(c//z)
v2=(a//x)*(b//z)*(c//y)

if v1>=v2:
	v2=v1
v1=(a//y)*(b//x)*(c//z)
if v1>=v2:
	v2=v1
v1=(a//y)*(b//z)*(c//x)
if v1>=v2:
	v2=v1
v1=(a//z)*(b//y)*(c//x)
if v1>=v2:
	v2=v1
v1=(a//z)*(b//x)*(c//y)
if v1>=v2:
	v2=v1
print(v2)