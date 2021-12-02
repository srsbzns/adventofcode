import pandas as pd

# create dataframe
with open('input.txt', 'r') as f:
    df = pd.read_table(f, sep='\\n', header=None, names=['depths'])

# calculate depth value differences
df['increases']=df['depths']>df['depths'].shift(1)

# calculate and report total increases
print(df['increases'].value_counts())