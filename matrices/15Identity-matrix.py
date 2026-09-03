""" 

=> Indentity Matrix 

    -> An indentity matrix is a square matrix 

    -> Main diagonal elements are 1 

    -> Every other daigonal elements are 0


"""


class Solution:

    def is_identity(self , matrix :list[list[int]]) -> bool:

        n = len(matrix)

        m = len(matrix[0])

        if n != m:           # not a square matrix
            return False

        for rows in range(n):
            for cols in range(m):

                if rows == cols:

                    if matrix[rows][cols] != 1:
                        return False

                else:

                   if matrix[rows][cols] != 0:
                       return False     

        return True


def main() -> None:
    matrix = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]

    solution = Solution()

    print(solution.is_identity(matrix))


if __name__ == "__main__":
    main()    