import numpy as np
from math import log

arr1 = np.array([10, 20, 30, 40, 50, 80])
arr2 = np.array([3, 7, 9, 8, 2, 27])
modulus = np.mod(arr1, arr2)

x = [12] 
y = [6]
res = np.divmod(x, y)

arr = np.trunc([-3.1666, 3.6667])
print(arr)
arr = np.ceil([-3.1666, 3.6667])
print(arr)
arr = np.floor([-3.1666, 3.6667])
print(arr)
arr = [-3.1666, 3.6667]
print(np.around(arr, 1))

#taking logarithm of a number in ndarray
arr = np.array([1, 2, 3, 4])
print(np.log10(arr))

print(log(16, 2))
nplog = np.frompyfunc(log, 2, 1)
print(nplog([16, 4], 2))