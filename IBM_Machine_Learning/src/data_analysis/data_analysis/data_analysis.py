import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# get data from a random repository
d = sns.load_dataset("tips")
data = pd.DataFrame(d["tip"])
plt.hist(data, bins=25)


dataset_names = sns.get_dataset_names()

# sample method catch data in the same proportion os the complete dataset
sample = data.sample(n=150, replace=False)
plt.hist(sample, bins=25)
plt.show()

print("Hola")

# plotting data
plt.plot(d.tip, d.total_bill, ls='', marker='o')
plt.show()

plt.plot(d.tip, d.sex, ls='', marker='o', label='sex')
plt.plot(d.tip, d.total_bill, ls='', marker='o', label='total_bill')
plt.legend()
plt.show()

result = d.groupby('day').mean()
d.groupby('day').mean().plot(color=['red', 'blue', 'black', 'green'], fontsize=10.0, figsize=(4,4))
plt.show()

sns.pairplot(d, hue='day')
plt.show()

sns.jointplot(d.tip, d.total_bill, kind='hex')
plt.show()

plot = sns.FacetGrid(d, col='day', margin_titles=True)
plot.map(plt.hist, 'tip', color='red')
plt.show()