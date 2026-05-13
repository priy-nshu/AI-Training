import numpy as np

def remove_invalid_rows(arr):
    arr = arr.astype(float)
    mask = np.all(np.isfinite(arr), axis=1)

    return arr[mask]

# Example
data = np.array([
    [1, 2, 3],
    [4, np.nan, 6],
    [7, 8, np.inf],
    [9, 10, 11]
])

clean_data = remove_invalid_rows(data)
print(clean_data)


def transpose_matrix(matrix):
    return matrix.T

mat = np.array([[1, 2, 3],
                [4, 5, 6]])

print(transpose_matrix(mat))


def highest_paid_employee():
    dtype = [('name', 'U20'), ('age', 'i4'), ('salary', 'f8')]

    employees = np.array([
        ('Alice', 30, 70000),
        ('Bob', 45, 85000),
        ('Charlie', 28, 65000),
        ('David', 40, 9000)
    ], dtype=dtype)

    max_salary_index = np.argmax(employees['salary'])
    return employees[max_salary_index]

highest = highest_paid_employee()
print("Highest paid employee:", highest)