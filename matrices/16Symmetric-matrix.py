""" 

=> Symmetric Matrix 

    -> A symmetric matrix is a square matrix that remains the same aftere transpose 

            A  =  AT



"""

class Solution:

    def is_symmetric(self , matrix : list[list[int]]) -> bool:

        n = len(matrix)

        m = len(matrix[0])

        if n != m:        # not square matrix
            return False


        for rows in range(n):
            for cols in range(m):

                if matrix[rows][cols] != matrix[cols][rows]:
                    return False
        return True

def main() -> None:
    matrix = [
        [1, 2, 3],
        [2, 4, 5],
        [3, 5, 6]
    ]

    solution = Solution()

    print(solution.is_symmetric(matrix))


if __name__ == "__main__":
    main()
            