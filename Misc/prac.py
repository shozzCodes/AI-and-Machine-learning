import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

# Simulate rolling 3 dice 10,000 times
dice1 = np.random.randint(1, 7, 10000)
dice2 = np.random.randint(1, 7, 10000)
dice3 = np.random.randint(1, 7, 10000)

# Calculate the sum of each roll
sums = dice1 + dice2 + dice3

# Plot the distribution
sns.histplot(
    sums,
    bins=np.arange(2.5, 19.5, 1),
    stat="probability",
    kde=True
)

plt.title("Distribution of the Sum of 3 Dice (10,000 Rolls)")
plt.xlabel("Sum of 3 Dice")
plt.ylabel("Probability")
plt.xticks(range(3, 19))
plt.grid(axis="y", alpha=0.3)
plt.show()

# Display statistics
print("Mean:", np.mean(sums))
print("Standard deviation:", np.std(sums))
print("Minimum sum:", np.min(sums))
print("Maximum sum:", np.max(sums))