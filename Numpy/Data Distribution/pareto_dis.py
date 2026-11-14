from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

x = random.pareto(3, size=10000)
sns.histplot(x, kde=False, bins=np.arange(-0.5, 20, 0.25))
plt.show()