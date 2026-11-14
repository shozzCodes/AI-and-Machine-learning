import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

marks = np.random.normal(loc=70, scale=10, size=10000)
sns.histplot(marks, kde=True, bins=np.arange(-5, 100, 10))
plt.xlabel("Marks")
plt.ylabel("Frequency")
print(marks[:10])
first_dev = np.mean((marks >= 60) & (marks <= 80))
second_dev = np.mean((marks >= 50) & (marks <= 90))
third_dev = np.mean((marks >= 40) & (marks <= 100))
print(first_dev * 100)
print(second_dev * 100)
print(third_dev * 100)
plt.show()

# data = np.random.normal(loc=15, scale=10, size=100)
# sns.displot(data, kind='hist')
# plt.show()