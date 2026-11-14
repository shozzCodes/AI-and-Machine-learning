import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import random

x = random.chisquare(df=1, size=1000)
sns.displot(x, kind='kde')
plt.show()