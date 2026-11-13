import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from numpy import random

x = random.normal(loc=5, scale=1, size=(8))

sns.displot(x, kind='kde')
plt.show()

# sns.displot([1,1])
# plt.show()