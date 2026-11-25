import numpy as np
def skewness(data:np.array):
    ans = None
    mean = np.mean(data)
    x = np.array([mean]*len(data))
    ans = data - x
    res = ans*ans
    sd = np.sqrt((sum(res) / len(data)))
    return sd
data = np.array([2.5, 3.7, 6.6, 9.1, 9.5, 10.7, 11.9, 21.5, 22.6, 25.2])

print(skewness(data))