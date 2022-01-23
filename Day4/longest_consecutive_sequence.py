class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dict1 = {}
        for num in nums:
            dict1[num]=1
        res = 0
        for num in nums:
            if num-1 not in dict1.keys():
                curr_num = num
                curr_str = 1
                
                while (curr_num+1) in dict1.keys():
                    curr_num+=1
                    curr_str+=1
                    
                res = max(res,curr_str)
                
        return res
