

class Solution:

    def transpose(self, matrix : list[list[int]]) -> list[int]:

        rows = len(matrix)
        cols = len(matrix[0])

        # original rows * cols 

        # tranpose cols * rows 

        transpose = [[0]* rows  for _ in range(cols)]

        for row in range(rows):
            for col in range(cols):

                transpose[col][row] = matrix[row][col]

        return transpose

def main() -> None:
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    solution = Solution()
    result = solution.transpose(matrix)

    for row in result:
        print(row)


if __name__ == "__main__":
    main()            