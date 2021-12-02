import pandas as pd

# create dataform
with open('input.txt', 'r') as f:
    df = pd.read_table(f, sep='\\n', header=None, names=['depths'])

# calculate 3-reading rolling windows
df['roll_sum_3']=df['depths'].rolling(3).sum()

#calcuate window increases
df['increase']=df['roll_sum_3']>df['roll_sum_3'].shift(1)

#calculate total increases and show output
print(df)
print(df.value_counts(subset='increase'))
