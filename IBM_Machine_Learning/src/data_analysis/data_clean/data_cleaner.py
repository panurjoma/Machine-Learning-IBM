

import seaborn as sns
import numpy as np
import scipy as scp
import pandas as pd
import matplotlib.pyplot as plt

# SQLITE
import sqlite3 as sq3
path = "../data/classic_rock.db"
# Create connection to database
con = sq3.Connection(path)
# write query
query = '''SELECT * FROM rock_songs'''
# Execute query
data = pd.read_sql(query, con)
data = list(data["PlayCount"])
# detecting outliers
q25, q50, q75 = np.percentile(data, [20, 50, 75])

# plot data
#plt.hist(data, bins=10)
#plt.show()

sns.displot(data)

print("Hola")