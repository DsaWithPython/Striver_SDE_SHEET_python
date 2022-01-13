import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum1 = 0
        maxi = -sys.maxsize-1
        for i in nums:
            sum1 += i
            maxi = max(sum1, maxi)
            if sum1<0:
                sum1=0
                
        return maxi
        
        
