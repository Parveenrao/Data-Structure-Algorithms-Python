# Row - wise traverse matrix 


class Traverse:

    def row_traverse(self , matrix : list[list[int]]) -> None:

        if not matrix or not matrix[0]:
            print("Matrix is empty")
            return
        

        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                print(matrix[i][j] , end = " ")

            print()


traverse = Traverse()

matrix = [

    [1, 2, 3],
    [3, 4, 5],
    [6, 7, 8]
]

traverse.row_traverse(matrix)