class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        def mergeSort(nums, low, high):
            if low>=high:
                return 0
            mid = low + (high-low)//2
            inv_count = mergeSort(nums, low, mid)
            inv_count += mergeSort(nums, mid+1, high)
            inv_count += merge(nums, low, mid, high)
            return inv_count
        
        def merge(nums, low, mid, high):
            cnt = 0
            j = mid + 1
            for i in range(low,mid+1):
                while j<=high and nums[i]>(2*nums[j]):
                    j+=1
                cnt+=(j-(mid+1))
            left = low
            right = mid+1
            temp = []
            while left<=mid and right<=high:
                if nums[left]<=nums[right]:
                    temp.append(nums[left])
                    left+=1
                else:
                    temp.append(nums[right])
                    right+=1
            while left<=mid:
                temp.append(nums[left])
                left+=1
            while(right<=high):
                temp.append(nums[right])
                right+=1
            for i in range(low, high+1):
                nums[i] = temp[i-low]
            return cnt
    
        return mergeSort(nums, 0, len(nums)-1)
        
