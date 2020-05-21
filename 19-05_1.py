class Matrix:
    def __init__(self, matrix_1, matrix_2):
        # self.matr = [matrix_1, matrix_2]
        self.matrix_1 = matrix_1
        self.matrix_2 = matrix_2

    def __add__(self):
        matr = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.matrix_1)):

            for j in range(len(self.matrix_2[i])):
                matr[i][j] = self.matrix_1[i][j] + self.matrix_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))


    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))



my_matrix = Matrix([[8, 3, 1],
                    [9, 4, 3],
                    [0, 5, 1]],
                   [[1, 8, 2],
                    [6, 7, 9],
                    [2, 5, 9]])
# result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


print(my_matrix.__add__())