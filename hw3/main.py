import numpy as np
from matrix import Matrix
from matrix_advanced import MatrixAdvanced

def solve_3_1():
    np.random.seed(0)

    A_data = np.random.randint(0, 10, (10, 10))
    B_data = np.random.randint(0, 10, (10, 10))

    A = Matrix(A_data)
    B = Matrix(B_data)

    C_add = A + B
    C_add.save_to("artifacts/task_1/matrix+.txt")

    C_mul = A * B
    C_mul.save_to("artifacts/task_1/matrix*.txt")

    C_matmul = A @ B
    C_matmul.save_to("artifacts/task_1/matrix@.txt")


def solve_3_2():
    np.random.seed(0)

    A_data = np.random.randint(0, 10, (10, 10))
    B_data = np.random.randint(0, 10, (10, 10))

    A = MatrixAdvanced(A_data)
    B = MatrixAdvanced(B_data)

    C_add = A + B
    C_mul = A * B
    C_matmul = A @ B

    C_add.save_to("artifacts/task_2/matrix+.txt")
    C_mul.save_to("artifacts/task_2/matrix*.txt")
    C_matmul.save_to("artifacts/task_2/matrix@.txt")


def generate_collision():
    while True:
        A_col = Matrix(np.random.randint(0, 5, (3, 3)))
        C_col = Matrix(np.random.randint(0, 5, (3, 3)))
        if hash(A_col) == hash(C_col) and not np.array_equal(A_col._data, C_col._data):
            break

    B_col = Matrix(np.random.randint(0, 5, (3, 3)))
    D_col = B_col

    AB = A_col @ B_col
    CD = C_col @ D_col
    if not np.array_equal(AB._data, CD._data):
        return A_col, B_col, C_col, D_col, AB, CD


def solve_3_3():
    np.random.seed(0)

    A_col, B_col, C_col, D_col, AB, CD = generate_collision()

    A_col.save_to("artifacts/task_3/A.txt")
    B_col.save_to("artifacts/task_3/B.txt")
    C_col.save_to("artifacts/task_3/C.txt")
    D_col.save_to("artifacts/task_3/D.txt")
    AB.save_to("artifacts/task_3/AB.txt")
    CD.save_to("artifacts/task_3/CD.txt")

    with open("artifacts/task_3/hash.txt", "w") as f:
        f.write(f"Hash(AB): {hash(AB)}\n")
        f.write(f"Hash(CD): {hash(CD)}\n")



if __name__ == '__main__':
    solve_3_1()
    solve_3_2()
    solve_3_3()
