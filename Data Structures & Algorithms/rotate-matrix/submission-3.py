class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 1. reverse: first row <-> last row
        matrix.reverse()

        # 2. transpose by swap the val acro diagonal line
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        





        