# CSV
import pandas as pd
"""
filepath = ""
data = pd.read_csv(filepath)
# or
# data = pd.read_csv(filepath, sep='\t')
# or
# data = pd.read_csv(filepath, delim_whitespace=True)
# etc
# reading some files only
print(data.iloc[:5])


# JSON
data = pd.read_json(filepath)
# dataframe to JSON
data.to_json('outputfile.json')


# SQLITE
import sqlite3 as sq3

# Create connection to database
con = sq3.Connection(path)
# write query
query = '''SELECT * FROM rock_songs'''
# Execute query
data = pd.read_sql(query, con)

"""

""" Here include which is indicated in the video to read a non SQL database with mongo for example where inside a 
table we have different connections. 
"""



# Now in API online public data
path_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df = pd.read_csv(path_url, header=None)

print("hola")