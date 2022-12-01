class Solution:
    
    def checkIsAP(self, arr, n):
        arr = sorted(arr)
        diff = arr[1]-arr[0]
        for i in range(1,len(arr)):
            if arr[i]-arr[i-1]!=diff:
                return False
        return True