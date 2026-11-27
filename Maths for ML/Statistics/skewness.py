import numpy as np
from scipy.stats import skew

def skewness(data:np.array):
    mean = np.mean(data)
    median = np.median(data)
    ans = (3*(mean - median)) / np.std(data)
    return ans

data = np.array([2.5, 3.7, 6.6, 9.1, 9.5, 10.7, 11.9, 21.5, 22.6, 25.2])

print(skewness(data))
print(skew(data, bias=False))