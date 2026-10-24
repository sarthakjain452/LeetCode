class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        zero_rows = set()
        zero_cols = set()

        # Find all rows and columns containing zero
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        # Set the corresponding rows and columns to zero
        for i in range(rows):
            for j in range(cols):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0
