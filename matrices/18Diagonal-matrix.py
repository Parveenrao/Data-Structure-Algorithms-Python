""" 

=> Diagonal Matrix 

    -> A Diagonal matrix is square matrix where every element outside the main
       diagonal is 0




"""


class Solution:

    def is_diagonal_matrix(self , matrix : list[list[int]]) -> bool:

        n = len(matrix)
        m = len(matrix[0])


        if n != m:       # first check for square matrix
            return False


        for row in range(n):
            for col in range(m):

                if row != col and matrix[row][col] != 0:
                    return False
        return True        



def main() -> None:

    matrix = [
         [5, 0, 0],
         [0, 8, 0],
         [0, 0, 3]
        ]

    obj = Solution()

    if obj.is_diagonal_matrix(matrix):
        print("Diagonal Matrix")
    else:
        print("Not a Diagonal Matrix")    

if __name__ == "__main__":
    main()        