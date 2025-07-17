
"""
import statistics

data = [2,2,6,10]
print(data)

mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)


print("Means:",mean)
print("Median",median)
print("Mode:",mode)

"""
# Representing a sparse matrix using a dictionary
sparse_matrix = {
    (0, 4): 5,
    (1, 2): 3,
    (3, 1): 7,
    (4, 0): 9
}

# Accessing an element at (row 0, column 4)
print(sparse_matrix.get((0, 4), 0))  # Output: 5 (non-zero value)

# Accessing an element at (row 2, column 2) which is 0
print(sparse_matrix.get((2, 2), 0))  # Output: 0 (zero value)
