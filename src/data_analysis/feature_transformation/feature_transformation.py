from numpy import log, log1p
from scipy.stats import boxcox
from sklearn.preprocessing import PolynomialFeatures
import seaborn as sns
import matplotlib.pyplot as plt
import math
import pandas as pd

# this functions will help us to transform skewed data in normal distributions.
data_filepath = "../data/iris_data.csv"
data = pd.read_csv(data_filepath)
# sns.displot(data['sepal_width'], bins=20)
# plt.show()
log_data = [math.log(d) for d in data['sepal_width']]
# sns.displot(log_data, bins=20)
# plt.show()

# using polynomial fetures
polyfeat = PolynomialFeatures(degree=2)
polyfeat = polyfeat.fit(data['sepal_width'])
x_poly = polyfeat.transform(data['sepal_width'])

# Variable selection.
# Another thing to do is encode the data in casa that data is nos numericall
# there are 2 different of non-numerical data: With ordered categories (high, medium, low) or with
# not ordered (red, blue, green)

# binary encoding (0 or 1)(in case of only 2 options
# one-hot encoding (separate all possible values and put one on the column that is true (0,1,0) )
# ordering encoding (for ordered categories)

# see why is important to scale data as well.
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.preprocessing import LabelEncoder, LabelBinarizer, OneHotEncoder
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import OrdinalEncoder
from pandas import get_dummies