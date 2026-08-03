"""

=> Transpose of Square matrix 


"""

class Solution:

    def transpose(self, matrix : list[list[int]]) -> list[list[int]]:

        n = len(matrix)

        for rows in range(n):
            for cols in range(rows + 1 , n):

                matrix[rows][cols] , matrix[cols][rows] = matrix[cols][rows] , matrix[rows][cols]


def main() -> None:
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    solution = Solution()
    solution.transpose(matrix)

    for row in matrix:
        print(row)


if __name__ == "__main__":
    main()
