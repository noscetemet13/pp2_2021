class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a=1
        b=0
        n=str(n)
        for i in n:
            a*=int(i)
            b+=int(i)
        return(a-b)