class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        flag = 0
        for k in range(n-2,-1,-1):
            if nums[k]<nums[k+1]:
                flag=1
                break
        if flag==0:
            nums.reverse()
        else:
            for l in range(n-1,k,-1):
                if nums[l]>nums[k]:
                    break
            nums[k],nums[l]=nums[l],nums[k]
            nums[k+1:]=reversed(nums[k+1:])
