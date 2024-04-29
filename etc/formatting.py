import pandas as pd

df = pd.read_csv('duckduck_tutorial.csv')

result_df = df[['title', 'href']]

result_df.to_csv('formatted.csv', index=False)




