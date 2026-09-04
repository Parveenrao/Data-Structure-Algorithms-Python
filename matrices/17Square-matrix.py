"""

=> Square matrix 

   -> No of rows and columns must be equal


"""


class Solution:

    def isSquareMatrix(self , matrix : list[list[int]]) -> int:

        rows = len(matrix)

        if rows == 0:      # empty matrix, square matrix
            return True


        for row in matrix:

            if len(row) != rows:
                return False
        return True

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

obj = Solution()

if obj.isSquareMatrix(matrix):
    print("Square Matrix")
else:
    print("Not a Square Matrix")        


# Time complexity = O(n) -> we travers only row 

# space complexity = O(1)