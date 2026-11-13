import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# record = np.random.poisson(lam=5, size=1000)
# sns.histplot(record, bins=np.arange(0,15)-0.5)
# plt.xlabel('Value')
# plt.ylabel('Frequency')
# plt.title('Poisson Distribution')
# plt.show()
data = np.random.poisson(lam=5, size=10000)

plt.hist(data, bins=np.arange(-0.5, max(data)+1.5, 1),
         density=True, edgecolor="black")

plt.title("Poisson Distribution")
plt.xlabel("Number of Events")
plt.ylabel("Probability")
plt.show()