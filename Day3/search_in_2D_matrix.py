class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo = 0
        if len(matrix)==0:
            return False
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        hi = (n_rows * n_cols)-1
        while lo<=hi:
            mid = (lo + (hi-lo)//2)
            row = mid//n_cols
            col = mid%n_cols
            
            if matrix[row][col] == target:
                return True
            elif matrix[row][col]<target:
                lo = mid+1
            else:
                hi = mid-1
        return False
