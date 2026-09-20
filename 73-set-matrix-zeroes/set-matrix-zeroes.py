class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        r= len(matrix)
        c = len(matrix[0])
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    self.mark_inf(matrix , i , j)
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == float("inf"):
                    matrix[i][j] = 0
    def mark_inf(self,matrix , row , col):
        r= len(matrix)
        c = len(matrix[0])
        for i in range(r):
            if matrix[i][col] != 0:
                matrix[i][col] = float("inf")
            
        for i in range(c):
            if matrix[row][i] != 0:
                matrix[row][i] = float("inf")