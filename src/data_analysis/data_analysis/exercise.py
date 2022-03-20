import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_filepath = "data/iris_data.csv"
data = pd.read_csv(data_filepath)

# Question 1
print(data.shape[0])

print(data.columns.tolist())

print(data.dtypes)

print(data.head(3))

print(data.value_counts('species'))

# Question 3
stats = data.sepal_length.describe(percentiles=[.25, 0.5, 0.75, 1])
print(data.sepal_length.describe(percentiles=[.25, 0.5, 0.75, 1]))
plt.hist(data.sepal_length, bins=30)
# sns.displot(data.sepal_length)

stats = data.sepal_width.describe(percentiles=[.25, 0.5, 0.75, 1])
print(data.sepal_width.describe(percentiles=[.25, 0.5, 0.75, 1]))
plt.hist(data.sepal_length, bins=30)

stats = data.petal_length.describe(percentiles=[.25, 0.5, 0.75, 1])
print(data.petal_length.describe(percentiles=[.25, 0.5, 0.75, 1]))
plt.hist(data.sepal_length, bins=30)

stats = data.petal_width.describe(percentiles=[.25, 0.5, 0.75, 1])
print(data.petal_width.describe(percentiles=[.25, 0.5, 0.75, 1]))
plt.hist(data.sepal_length, bins=30)
plt.show()

# final data management
stats = data.describe()
stats.loc['range'] = stats.loc['max'] - stats.loc['min']
out_fields = ['mean','25%','50%','75%', 'range']
stats_df = stats.loc[out_fields]
stats_df.rename({'50%': 'median'}, inplace=True)

# Question 4
print(data.groupby('species').mean())
print(data.groupby('species').median())

# in one step to execute different operations at a time.
grouped_data = data.groupby('species').agg([np.mean, np.median])

# or

from pprint import pprint

agg_dict = {field: ['mean', 'median'] for field in data.columns if field != 'species'}
agg_dict['petal_length'] = 'max'
pprint(agg_dict)
grouped_data = data.groupby('species').agg(agg_dict)


# Question 5
plt.plot(data.sepal_length, data.sepal_width, ls='', marker='o', label='sepal')
plt.ylabel("sepal_width")
plt.xlabel("sepal_length")
plt.title("Sepal Length vs Width")
plt.legend()
plt.show()

# or
ax = plt.axes()
ax.scatter(data.sepal_length, data.sepal_width)
ax.set(xlabel='Sepal Length (cm)',
       ylabel='Sepal Width (cm)',
       title='Sepal Length vs Width')
plt.show()

# Question 6
plt.subplot(221)

# equivalent but more general
ax1 = plt.subplot(2, 2, 1)
plt.hist(data.sepal_width)

# add a subplot with no frame
ax2 = plt.subplot(2, 2, 2)
plt.hist(data.sepal_length)

# add a polar subplot
plt.subplot(2, 2, 3)
plt.hist(data.petal_width)

# add a red subplot that shares the x-axis with ax1
plt.subplot(2, 2, 4)
plt.hist(data.petal_length)
plt.show()

# Question 7
ax = data.plot.hist(bins=25, alpha=0.5)
ax.set_xlabel('Size (cm)')
plt.show()

# or
axList = data.hist(bins=25)
# Add some x- and y- labels to first column and last row
for ax in axList.flatten():
    if ax.is_last_row():
        ax.set_xlabel('Size (cm)')
    if ax.is_first_col():
        ax.set_ylabel('Frequency')
plt.show()

# Question 8
data.boxplot(by='species')
plt.show()

# Question 9
data.set_index('species').stack().to_frame().reset_index()
print("stop")
plot_data = (data
             .set_index('species')
             .stack()
             .to_frame()
             .reset_index()
             .rename(columns={0:'size', 'level_1':'measurement'})
            )
plot_data.head()
sns.set_style('white')
sns.set_context('notebook')
sns.set_palette('dark')
f = plt.figure(figsize=(6,4))
sns.boxplot(x='measurement', y='size',
            hue='species', data=plot_data)
plt.show()

# Question 10
sns.set_context('talk')
sns.pairplot(data, hue='species')
plt.show()

print("Hi")