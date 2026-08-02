""" 

=> Upper-Triangle Matrix 


     -> An upper trinagle matrix is a sqaure matrix , where every element below the 
        main diagonal is 0:


"""


class Solution:

    def is_uppertriangle(self, matrix : list[list[int]]) -> int:  

        n = len(matrix)
        m = len(matrix[0])


        if n != m:          # first check , square matrix
            return False

        for rows in range(n):
            for cols in range(m):

                if rows > cols and matrix[rows][cols] != 0:
                    return False
        return True        