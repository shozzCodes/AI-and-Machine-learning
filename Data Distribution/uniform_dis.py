from numpy import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


x = random.uniform(low=1, high=6, size=1000)
sns.histplot(x, bins=30, kde=True)
plt.title('Uniform Distribution')
plt.show()