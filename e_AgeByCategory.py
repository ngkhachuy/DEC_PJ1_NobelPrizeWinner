import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('data/nobel.csv')

data.dropna(subset=['birth_date'], inplace=True)
data['year_birthday'] = data['birth_date'].transform(lambda x: str(x)[0:4])
data.loc[:, 'year_birthday'] = pd.to_numeric(data.loc[:, 'year_birthday'])
data['year_old'] = data['year'] - data['year_birthday']
data = data.loc[:, ['year', 'year_old', 'category']]
data = pd.pivot_table(data, index=['year'], columns='category', values='year_old')
data = data.reset_index()

columns = data.columns.drop(data.columns[0])

fig, ax = plt.subplots(nrows=6, ncols=1)
i = 0
for x in columns:
    ax[i].plot()
    data.loc[:, ['year', x]].plot.scatter(x='year', y=x, ax=ax[i])
    i += 1

plt.show()
