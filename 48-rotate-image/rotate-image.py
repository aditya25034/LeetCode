class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        res = [[0]*rows for _ in range(cols)]
        row = len(matrix)
        col = len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res[j][i] = matrix[i][j]
        for i in range(len(matrix)):
            res[i].reverse()
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] = res[i][j]