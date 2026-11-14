import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

x = np.random.zipf(a=2.5, size=1000)
sns.displot(x, kind='hist', bins=30, kde=True)
plt.title('Zipf Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()