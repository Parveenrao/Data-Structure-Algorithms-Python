""" 


=> Print Digonal / Main Elements of a matrices



"""


class Solution:

    def diagonal_elements(self , matrix : list[list[int]]) -> None:

        if not matrix or not matrix[0]:
            return

        rows = len(matrix)

        for i in range(rows):
            print(matrix[i][i])


def main() -> None:

    matrix : list[list[int]] = [


        [1, 2, 3],
        [3, 4, 5],
        [5, 6, 7]
    ]

    solution = Solution()

    solution.diagonal_elements(matrix)

if __name__ == "__main__":
    main()    



