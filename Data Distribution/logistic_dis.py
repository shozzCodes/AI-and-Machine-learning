import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import random

x = random.logistic(loc=1, scale=2, size = 1000)
sns.displot(x, kind='kde', fill=True)
plt.show()
