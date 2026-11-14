import numpy as np
from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt
# A binomial distribution tells us the probability of getting a particular number of successes in a fixed number of independent trials.
# Fixed number of trials (n)
# Two possible outcomes
# Constant probability (p)
# Independent trials (size)

# coin = random.binomial(n=20, size=1000, p=0.5)
# print("mean: ", np.mean(coin))
# print("max: ", np.max(coin))
# print("min: ", np.min(coin))
# sns.histplot(coin, kde=False, bins=np.arange(-0.5, 21.5, 1))
# plt.xlabel("No. of heads")
# plt.ylabel("Frequency")
# plt.show()

score = random.binomial(n=15, size=5000, p=0.6)
sns.histplot(score, edgecolor="black", bins=np.arange(-0.5, 16.5,1))
plt.xlabel("No. of correct answers")
plt.ylabel("Frequency")
print("Avg correct answers: ", np.mean(score))
print("Standard Deviation: ", np.std(score))
print("Maximum correct answers: ", np.max(score))
plt.show()