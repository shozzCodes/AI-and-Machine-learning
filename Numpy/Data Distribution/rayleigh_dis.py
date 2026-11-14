from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

x = random.rayleigh(scale=3, size=10000)
sns.displot(x, kind='kde')
print(x.mean())


plt.show()