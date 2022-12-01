class Solution(object):
    def singleNumber(self, nums):
        f={}
        for i in nums:
            if(i in f):
                f[i]+=1
            else:
                f[i]=1
        l=[]
        for i in f:
            if(f[i]==1):
                l.append(i)
        return l