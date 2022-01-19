class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        dict1 = {}
        n = len(nums)
        for i in range(0,n):
            if target-nums[i] in dict1.keys():
                ans.append(dict1[target-nums[i]])
                ans.append(i)
                return ans
            dict1[nums[i]]=i
        return ans
                    
        
