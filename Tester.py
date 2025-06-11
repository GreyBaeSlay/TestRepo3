import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'A': ["Hey", 2, "THere"],
    'B': [4, 5, 6]
})

df2 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [0, 1, 2]
})

# List with a variable (col) which may contain invalid column names
cols = [1,2]  # 'C' doesn't exist in the DataFrame

# Filter out invalid columns using .isin()
valid_cols = [col for col in cols if col in df.columns]

# Now you can loop through only valid columns
#for col in valid_cols:
    #print(df.loc[:, col])  # No warning will be raised

filtered_df = df[df.apply(lambda row: row.isin(cols).any(), axis=1)]
#print(filtered_df)
#otherf = df.loc(cols)

filtered_df = df.reindex(list(cols)).dropna(how='all')  # Drop fully NaN rows (missing indexes)
#print(filtered_df)

df = df.where(df.notnull(), None)
#print(df)

indicies = df2['B']

values = set(df.loc[indicies.tolist(), 'A'])

print(type(values))
print()