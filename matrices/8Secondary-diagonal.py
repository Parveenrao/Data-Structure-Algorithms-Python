class Solution:

    def secondary_diagonal(self , matrix : list[list[int]]) -> None:

        if not matrix or not matrix[0]:
            return


        rows = len(matrix)
        cols = len(matrix[0])
 
        for i in range(rows):                 # for rectangular matrix, we use min(rows , cols)
            print(matrix[i][cols-1-i])

def main() -> None:

    matrix: list[list[int]] = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    solution = Solution()
    solution.secondary_diagonal(matrix)


if __name__ == "__main__":
    main()
