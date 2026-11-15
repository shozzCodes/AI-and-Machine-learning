import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

grid = np.random.randint(1, 100, size=(5,5))
print(grid)
x = np.random.normal(loc=50, scale=10, size=1000)
sns.displot(x, kind='kde')
plt.show()