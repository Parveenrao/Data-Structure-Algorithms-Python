# Largest element in the  matrix 


class Element:

    def largest_element(self , matrix : list[list[int]]) -> int:

        if not matrix or not matrix[0]:
            raise ValueError('matrix is empty')
        
        rows = len(matrix)
        cols = len(matrix[0])

        max = matrix[0][0]

        for i in range(rows):
            for j in range(cols):

                if matrix[i][j] > max:
                    max = matrix[i][j]

        return max


ele = Element()


matrix = [
    [3, 8, 1],
    [5, 2, 9],
    [4, 7, 6]
]

print(ele.largest_element(matrix))