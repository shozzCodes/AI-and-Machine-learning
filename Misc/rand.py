from numpy import random
import numpy as np

arr = np.array([1,2,3,4,5])
x = np.random.randint(100, size=(4))
y = np.random.rand(2)
print(y)
print(arr)
print(x)
print(np.random.choice(arr))
two_dim_matrix = np.random.randint(2, size=(8,8))
print(two_dim_matrix)
z = np.random.choice([12,10,11,10], size=10)
print(z)

arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)
print(random.permutation(arr))

arr = random.choice([1,0], p=[0.2,0.8], size=(8,8))
print(arr)