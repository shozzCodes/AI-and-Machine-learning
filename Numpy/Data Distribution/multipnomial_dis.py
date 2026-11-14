import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

x = np.random.multinomial(n=100, pvals=[0.2, 0.3, 0.5], size=1000)
sns.displot(x, kind='hist', bins=30, kde=True)
plt.title('Multinomial Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()