class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lo = 0
        hi = len(nums)-1
        mid = 0
        
        while (mid<=hi):
            if nums[mid]==0:
                nums[lo],nums[mid]=nums[mid],nums[lo]
                lo+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            elif nums[mid]==2:
                nums[mid],nums[hi]=nums[hi],nums[mid]
                hi-=1
            
