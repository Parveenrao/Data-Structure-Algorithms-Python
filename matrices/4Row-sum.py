class Sum:

    def row_sum(self, matrix : list[list[int]]) -> None:

        if not matrix or not matrix[0]:
            print("Matrix is empty")
            return 
      
        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            row_sum = 0

            for j in range(col):

                row_sum += matrix[i][j]


            print(f"Row{i} Sum {row_sum}")   


sum = Sum()


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

sum.row_sum(matrix)




        
