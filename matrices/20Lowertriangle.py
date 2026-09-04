""" 

=> LowerTriangle Matrix 

    -> A lower triangle matrix is a square matrix where every element above the
       main diagonal is 0


"""

class Solution:

    def is_lower_triangular_matrix(self , matrix : list[list[int]]) -> int:

        n = len(matrix)

        m = len(matrix)

        if n != m:       # first check for square matrix
            return False


        for rows in range(n):
            for cols in range(m):


                if rows < cols and matrix[rows][cols] != 0:
                    return False

        return True        