""" 

=> Replace Secondary digonal with its sum


"""


class Solution:

    def replace_sum_secondary_diagonal(self, matrix : list[list[int]]) -> None:

        if not matrix or not matrix[0]:
            return 

        n = len(matrix)

        diagonal_sum = 0

        for i in range(n):
            diagonal_sum += matrix[i][n-1-i]

        for i in range(n):
            matrix[i][n-1-i] = diagonal_sum

def main() -> None:

    matrix: list[list[int]] = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    solution = Solution()
    solution.replace_sum_secondary_diagonal(matrix)

    for row in matrix:
        print(row)


if __name__ == "__main__":
    main()                