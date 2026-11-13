import numpy as np

# arr = np.array([23,12, 10])
# print(arr)
# arr = np.array([12,12,14,15], ndmin=2)
# print(arr.shape)
# new = arr.reshape(2,2)
# print(new)
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# narr = arr.reshape(2,4)
# print(narr)
arr0 = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
# print(arr)
# # for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
# #     print(x)

# for idx, x in np.ndenumerate(arr):
#     print(idx, x)
arr1 = np.array([[10, 20, 30]])
arr2 = np.array([40, 50, 60])
arr = np.concatenate((arr0,arr2), axis=3)
print(arr)