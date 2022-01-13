class Solution:
    def generate(self, numRows: int) -> List[List[int]]:        
        r = [[1 for i in range(numRows)] for j in range(numRows)]
        for i in range(0,numRows):
            r[i]=r[i][0:i+1]
            r[i][0]=1
            r[i][i]=1
            for j in range(1,i):
                r[i][j] = r[i-1][j-1] + r[i-1][j]
        return r
