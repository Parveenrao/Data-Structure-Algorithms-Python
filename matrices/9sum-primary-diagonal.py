""" 

=> Print the sum of primary digonal elements


"""


class Solution:

    def sum_primary_diagonal(self , matrix : list[list[int]]) -> int:

        if not matrix or not matrix[0]:
            return 0

        total_sum = 0

        rows = len(matrix)

        for i in range(rows):
            total_sum += matrix[i][i]

        return total_sum


def main() -> None:

    matrix : list[list[int]] = [
    
    
            [1, 2, 3],
            [3, 4, 5],
            [5, 6, 7]
        ]
    
    solution = Solution()
    
    print(solution.sum_primary_diagonal(matrix))


if __name__ == "__main__":
    main()



  