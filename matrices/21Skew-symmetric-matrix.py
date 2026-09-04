""" 

=> Skew-symmetric matrix 

    -> Is a square matrix where 
      
     AT = -A



     A[i][j]= -A[j][i]




"""


class Solution:

    def is_skew_symmetric_matrix(self, matrix : list[list[int]]) -> int:

        n = len(matrix)
        m = len(matrix[0])

        if n != m:            # first check for square matrix
            return False


        for rows in range(n):
            for cols in range(m):

                if matrix[rows][cols] != -matrix[cols][rows]:
                    return False

        return True        
        

        
