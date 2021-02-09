class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes=[]
        x=0
        altitudes+=[x]
        for i in gain:
            altitudes+=[x+i]
            x+=i
        maxi=-1e9
        for i in altitudes:
            if i>maxi:
                maxi=i
        return(maxi)