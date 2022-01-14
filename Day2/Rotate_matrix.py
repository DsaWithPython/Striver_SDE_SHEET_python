class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix) #3
        cols = len(matrix[0]) #3
        for i in range(rows): # 1
            for j in range(i,cols): # 2
                matrix[i][j],matrix[j][i] = matrix[j][i] ,matrix[i][j] 
        for i in range(0,rows):
            for j in range(0,(rows//2)):
                matrix[i][j],matrix[i][rows-1-j]=matrix[i][rows-1-j],matrix[i][j]
