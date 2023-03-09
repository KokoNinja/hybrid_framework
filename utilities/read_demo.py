"This file will be deleted. Not part of the framework"
#to understand how to read  CSV file

import pandas

df=pandas.read_csv(filepath_or_buffer="../test_data/test_invalid_login_data.csv",delimiter=";")
print(df)
print(list(df.loc[1]))
print(tuple(df.loc[0]))

print(df.loc[0].tolist())
print(df.index)

for i in df.index:
    print(df.loc[i].tolist())

print(df.values.tolist())

