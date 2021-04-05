a=list(map(int, input().split()))
b=int(input())%len(a)
print(*(a[-b:]+a[:-b]))