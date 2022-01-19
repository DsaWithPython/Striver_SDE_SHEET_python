class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        N = n + m - 2 # n-1 + m-1
        r = m - 1
        res = 1
        
        for i in range(1,r+1):
            res = res * (N - r + i)//i
        return res
