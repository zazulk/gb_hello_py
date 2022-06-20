class Matrix:

    def __init__(self, list_of_lists):
        self.matrix = list_of_lists.copy()

    def __str__(self):
        res = ""
        for lst in self.matrix:
            res += " ".join([str(i) for i in lst]) + "\n"
        return res

    def __add__(self, other):
        res = []
        for index in range(len(self.matrix)):
            r1 = []
            for i in range(len(self.matrix[index])):
                r1.append(self.matrix[index][i] + other.matrix[index][i])
            res.append(r1)
        return Matrix(res)


new_matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
new_matrix_2 = Matrix([[2, 3, 4], [5, 6, 7], [8, 9, 10]])
new_matrix_3 = Matrix([[3, 4, 5], [6, 7, 8], [9, 10, 11]])

print(new_matrix)
print(new_matrix_2)
print(new_matrix_3)

print(new_matrix + new_matrix_2 + new_matrix_3)

