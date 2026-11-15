import numpy as np

x = np.array([1, 2, 3, 4])
y = np.array([5, 6, 7, 8])
arr = np.random.randint(0,10, size=10)
print(arr)
print(np.add(x, y))
print(np.sum([x, y], axis=1))
print(np.cumsum([x, y]))
x = np.array([1, 2, 3, 4])
y = np.array([5, 6, 7, 8])
print(np.prod([x, y], axis=1))