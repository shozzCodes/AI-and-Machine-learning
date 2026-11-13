import numpy as np

arr = np.array([[12,13], [14,15]])
arr2 = np.array([[11,11], [10, 18]])
newArr = np.concatenate((arr,arr2), axis=1)
print(newArr)

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)
      
arr = np.array([1, 2, 3, 4, 5, 6, 7])
filtered = arr % 2 != 0
newArr = arr[filtered]
print(filtered)