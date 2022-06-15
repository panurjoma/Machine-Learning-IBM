from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.preprocessing import LabelEncoder, LabelBinarizer, OneHotEncoder
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import OrdinalEncoder
from pandas import get_dummies
from numpy import log, log1p
from scipy.stats import boxcox
from sklearn.preprocessing import PolynomialFeatures
import seaborn as sns
import matplotlib.pyplot as plt
import math
import pandas as pd
import numpy as np

## Load in the Ames Housing Data
datafile = "data/Ames_Housing_Data.tsv"
df = pd.read_csv(datafile, sep='\t')

## Examine the columns, look at missing data
df.info()

## Get the columns where the 'Gr Liv Area' is <= 4000
# This is recommended by the data set author to remove a few outliers
df = df.loc[df['Gr Liv Area'] <= 4000,:]
print("Number of rows in the data:", df.shape[0])
print("Number of columns in the data:", df.shape[1])
data = df.copy()  # Keep a copy our original data
df.info()

len(df.PID.unique())
# Dropping columns for whih every value is unique because we will not add any value to our eventual model.
df.drop(['PID', 'Order'], axis=1, inplace=True)

# A quick look at the data (only works on notebook):
df.head()

# to filter dataframe depending on columns types we have this manner
# df.select_dtypes('object').columns

# or this manner
# Get a Pd.Series consisting of all the string categoricals
types = df.dtypes
one_hot_encode_cols = df.dtypes[df.dtypes == object]  # filtering by string categoricals
one_hot_encode_cols = one_hot_encode_cols.index.tolist()  # list of categorical fields
print(df[one_hot_encode_cols].head().T)   # to transpose the dataframe

# first of all we do some basic data cleaning of the data.
# Do the one hot encoding
df = pd.get_dummies(df, columns=one_hot_encode_cols, drop_first=True)
print(df.describe())

# Create a list of float colums to check for skewing
mask = data.dtypes == float
# or
# mask = data.select_dtypes('number').columns
number_cols = data.columns[mask]
skew_limit = 0.75  # define a limit above which we will log transform
skew_vals = data[number_cols].skew()

# Showing the skewed columns
skew_cols = (skew_vals
             .sort_values(ascending=False)
             .to_frame()
             .rename(columns={0:'Skew'})
             .query('abs(Skew) > {}'.format(skew_limit)))
print(skew_cols)

# Let's look at what happens to one of these features, when we apply np.log1p visually.
# Choose a field
field = "SalePrice"

# Create two "subplots" and a "figure" using matplotlib
fig, (ax_before, ax_after) = plt.subplots(1, 2, figsize=(10, 5))

# Create a histogram on the "ax_before" subplot
df[field].hist(ax=ax_before)

# Apply a log transformation (numpy syntax) to this column
df[field].apply(np.log1p).hist(ax=ax_after)

# Formatting of titles etc. for each subplot
ax_before.set(title='before np.log1p', ylabel='frequency', xlabel='value')
ax_after.set(title='after np.log1p', ylabel='frequency', xlabel='value')
fig.suptitle('Field "{}"'.format(field))
plt.show()

# Perform the skew transformation:
for col in skew_cols.index.values:
    if col == "SalePrice":
        continue
    df[col] = df[col].apply(np.log1p)

# We now have a larger set of potentially-useful features
print(df.shape)

# There are a *lot* of variables. Let's go back to our saved original data and look at how many values are missing for each variable.
df = data
print(data.isnull().sum().sort_values())

# Lets pick out just a few numeric columns to illustrate basic feature transformations.
smaller_df = df.loc[:, ['Lot Area', 'Overall Qual', 'Overall Cond',
                        'Year Built', 'Year Remod/Add', 'Gr Liv Area',
                        'Full Bath', 'Bedroom AbvGr', 'Fireplaces',
                        'Garage Cars', 'SalePrice']]
# Now we can look at summary statistics of the subset data
print(smaller_df.describe().T)
print(smaller_df.info())

# There appears to be one NA in Garage Cars - we will take a simple approach and fill it with 0
smaller_df = smaller_df.fillna(0)
print(smaller_df.info())
# Lets plot the relationships between data columns and explore a little bit more to manipulate them.
# sns.pairplot(smaller_df, plot_kws=dict(alpha=.1, edgecolor='none'))
# plt.show()

# Suppose target variable is SalePrice
# Separate our features from our target
X = smaller_df.loc[:, ['Lot Area', 'Overall Qual', 'Overall Cond',
                       'Year Built', 'Year Remod/Add', 'Gr Liv Area',
                       'Full Bath', 'Bedroom AbvGr', 'Fireplaces',
                       'Garage Cars']]
y = smaller_df['SalePrice']
print(X.info())

#  We'll need to create a train/validation split before we fit and score the model.
"""One of the first things that we looked for in the pairplot was evidence about the relationship between each feature and the target. In certain 
features like 'Overall Qual' and 'Gr Liv Qual', we notice an upward-curved relationship rather than a simple linear correspondence. 
This suggests that we should add quadratic polynomial terms or transformations for those features, allowing us to express that 
non-linear relationship while still using linear regression as our model.
Luckily, pandas makes it quite easy to quickly add those square terms as additional features to our original feature set. We'll do so and evaluate our model again below.
As we add to our baseline set of features, we'll create a copy of the latest benchmark so that we can continue to store our older feature sets."""

# first model features
X2 = X.copy()
X2['OQ2'] = X2['Overall Qual'] ** 2
X2['GLA2'] = X2['Gr Liv Area'] ** 2

"""As is, each feature is treated as an independent quantity. However, there may be interaction effects, in which the
impact of one feature may dependent on the current value of a different feature.
For example, there may be a higher premium for increasing _'Overall Qual'_ for houses that were built more recently. If
such a premium or a similar effect exists, a feature that multiplies _'Overall Qual'_ by _'Year Built'_ can help us capture it.
Another style of interaction term involves feature proprotions: for example, to get at something like quality per square
foot we could divide 'Overall Qual' by 'Lot Area'.
Let's try adding both of these interaction terms and see how they impact the model results."""

# second model features
X3 = X2.copy()
# multiplicative interaction
X3['OQ_x_YB'] = X3['Overall Qual'] * X3['Year Built']
# division interaction
X3['OQ_/_LA'] = X3['Overall Qual'] / X3['Lot Area']

# We are going to incorporate categorical featutes to the model, starting with 'House Style'
data['House Style'].value_counts()
print(pd.get_dummies(df['House Style'], drop_first=True).head())
nbh_counts = df.Neighborhood.value_counts()
print(nbh_counts)

# For this category, let's map the few least-represented neighborhoods to an "other" category before adding the feature
# to our feature set and running a new benchmark.
other_nbhs = list(nbh_counts[nbh_counts <= 8].index)
print(other_nbhs)

# replace function is to change some values with other values in a particular column
X4 = X3.copy()
X4['Neighborhood'] = df['Neighborhood'].replace(other_nbhs, 'Other')

"""Let's close out our introduction to feature engineering by considering a more complex type of feature that may work 
very nicely for certain problems. It doesn't seem to add a great deal over what we have so far, but it's a style of
engineering to keep in mind for the future.
We'll create features that capture where a feature value lies relative to the members of a category it belongs to.
In particular, we'll calculate deviance of a row's feature value from the mean value of the category that row belongs
to. This helps to capture information about a feature relative to the category's distribution, e.g. how nice a house
is relative to other houses in its neighborhood or of its style.
Below we define reusable code for generating features of this form, feel free to repurpose it for future feature 
engineering work!"""

# important to know that transform function is similar to groupby function with the difference of applying the function
# to each row and not being limited to smaller dataframe.


def add_deviation_feature(X, feature, category):
    """
    eg: feature: Overall qual, category: Neigborhood
    feature: numerical values
    category: categorical values
    """
    # temp groupby object
    category_gb = X.groupby(category)[feature]

    # create category means and standard deviations for each observation
    category_mean = category_gb.transform(lambda x: x.mean())
    category_std = category_gb.transform(lambda x: x.std())

    # compute stds from category mean for each feature value,
    # add to X as new feature
    deviation_feature = (X[feature] - category_mean) / category_std
    X[feature + '_Dev_' + category] = deviation_feature


# Lets use our deviation feature generation
X5 = X4.copy()
X5['House Style'] = df['House Style']
add_deviation_feature(X5, 'Year Built', 'House Style')
add_deviation_feature(X5, 'Overall Qual', 'Neighborhood')

#  Instantiate and provide desired degree;
#  Note: degree=2 also includes intercept, degree 1 terms, and cross-terms
pf = PolynomialFeatures(degree=2)

features = ['Lot Area', 'Overall Qual']
pf.fit(df[features])
pf.get_feature_names_out()   # Must add input_features = features for appropriate names

feat_array = pf.transform(df[features])
pd.DataFrame(feat_array, columns=pf.get_feature_names(input_features=features))

print("hi world!")

