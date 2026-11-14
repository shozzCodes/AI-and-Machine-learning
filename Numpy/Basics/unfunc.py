import numpy as np

def vector_addition(x, y):
    return x+y

vector_addition = np.frompyfunc(vector_addition, 2, 1)

x = [1,2]
y = [3,4]
sum = vector_addition(x, y)
print(type(vector_addition)) 

