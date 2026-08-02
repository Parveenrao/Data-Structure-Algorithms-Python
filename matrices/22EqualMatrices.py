""" 

=> Check whether Two Matrices Are Equal 

    -> Two Matrices Are Equal when 

        1. They have same dimension
        2. Every element at the same position is equal

"""


class Solution:

    def is_equal(self , matrix1 : list[list[int]] , matrix2 : list[list[int]]) -> bool:

        n1 = len(matrix1)
        m1 = len(matrix1[0])

        n2 = len(matrix2)
        m2 = len(matrix2[0])


        if n1!= n2 or m1!= m2:  # Dimension must be equal
            return False


        for row in range(n1):
            for col in range(m1):


                if matrix1[row][col] != matrix2[row][col]:
                    return  False

        return True         