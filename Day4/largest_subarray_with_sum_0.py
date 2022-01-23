#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        max_len = 0
        sum1 = 0 #prefix sum
        dict1 = {}
        for i in range(0,n):
            sum1+=arr[i]
            if sum1 == 0:
                max_len = i + 1
            else:
                if sum1 in dict1.keys():
                    max_len = max(max_len,i-dict1[sum1])
                else:
                    dict1[sum1] = i
        return max_len
            

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends
