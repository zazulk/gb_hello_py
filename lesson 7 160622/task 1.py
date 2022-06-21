from itertools import zip_longest
from random import randint


class Matrix:
    matrix_store = []

    @staticmethod
    def show_matrix_store():
        return f"\n{'-'*30}\n".join([f"\033[1m{i})\033[0m\n"
                                     f"{Matrix.__str__(val)}" for i, val in
                                     enumerate(Matrix.matrix_store, 1)])

    def __init__(self, list_of_lists):
        self.matrix = list_of_lists
        Matrix.matrix_store.append(self)

    def __str__(self):
        return "\033[32m" + "\n".join(["\t\t".join([str(i) for i in lst]) for
                                       lst in self.matrix]) + "\033[0m"

    def __add__(self, other):
        new_m = zip_longest(self.matrix, other.matrix, fillvalue=[])
        return Matrix([map(sum, zip_longest(*m, fillvalue=0)) for m in new_m])

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)


for rand in range(randint(2, 4)):
    Matrix([[randint(-20, 20) for r_1 in range(randint(2, 4))] for r_2 in
            range(randint(2, 4))])

print(Matrix.show_matrix_store())
print("-" * 30)
print("\033[35mСумма всех матриц:")
try:
    print(f"{sum([*Matrix.matrix_store])}")
except Exception as err:
    print(err)
