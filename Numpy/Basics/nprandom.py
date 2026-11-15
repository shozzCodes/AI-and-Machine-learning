import numpy as np
# arr = np.array([1, 2, 3, 4])
x = np.array([10] * 11)
arr = np.random.rand(11)
print(x)
print(np.round(arr, 2))
arr = np.random.uniform(0, 10, size=11)
print(np.round(arr, 2))

board = np.random.choice(
    [1,0],
    p=[0.9, 0.1],
    size=(2,2)
)
print(board)
print(np.unique(board, return_counts=True))