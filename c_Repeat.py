import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/nobel.csv', usecols=['full_name'])
data = data.groupby(['full_name']).size().reset_index(name='count')
data = data.loc[data['count'] > 1, ['full_name', 'count']]

fig, ax = plt.subplots(figsize=(15, 15))
data.plot(x='full_name', y='count', kind='barh', ax=ax)
ax.set(xlabel='Prizes', ylabel='Names')
plt.show()
