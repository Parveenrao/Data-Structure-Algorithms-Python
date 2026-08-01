""" 

=> Rotate Matrix 90 degree clockwise 

    -> Transpose matrix and then reverse each row

"""

class Solution:

    def rotate(self , matrix : list[list[int]]) -> list[list[int]]:

        n = len(matrix)

        for i in range(n):
            for j in range(i + 1 , n):

                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]


        for row in matrix:
          

            left = 0 

            right = n-1

            while left < right:

                row[left], row[right] = row[right] , row[left]

                left += 1
                right -= 1



def main() -> None:
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    solution = Solution()

    print("Original Matrix:")
    for row in matrix:
        print(row)

    solution.rotate(matrix)

    print("\nMatrix after 90° Clockwise Rotation:")
    for row in matrix:
        print(row)


if __name__ == "__main__":
    main()


"""

=> Time Complexity for

    1. For transpose O(n*n)

    2. for rever 

       Thre are n rows and for one rows if we n/2 swaps 

       so (n*n)

       overl all O(N*N)

"""