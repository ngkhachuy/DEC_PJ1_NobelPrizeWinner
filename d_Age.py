import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('data/nobel.csv')

data.dropna(subset=['birth_date'], inplace=True)
data['year_birthday'] = data['birth_date'].transform(lambda x: str(x)[0:4])
data.loc[:, 'year_birthday'] = pd.to_numeric(data.loc[:, 'year_birthday'])
data['year_old'] = data['year'] - data['year_birthday']
data = data.loc[:, ['year', 'year_old']]

data_mean = data.groupby('year')
data_mean = data_mean['year_old'].mean()
data_mean = pd.concat([data_mean.head(1), data_mean.tail(1)])

ax = data.plot.scatter(x='year', y='year_old')
data_mean.plot(color='r')

ax.set(xlabel='year', ylabel='age')
ax.grid()
plt.show()
