import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
# data = np.array([45, 50, 52, 55, 56, 58, 60, 85, 90, 98, 96, 92, 90])
# sns.displot(data, kind='kde')
# norm = np.random.normal(size=10)
# sns.displot(np.random.normal(norm), kind='kde')

marks = np.random.normal(loc=70, scale=5, size=53)
y = norm.pdf(np.median(marks), loc=np.mean(marks), scale=np.median(marks))

sns.displot(marks, kind='kde')
plt.scatter(np.median(marks), y)
print(marks)
print("Mean: ", np.mean(marks))
print("PDF: ", y)
plt.show()
