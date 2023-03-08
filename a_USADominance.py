import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Read data
data = pd.read_csv('data/nobel.csv')

# Create column 'decade' from 'year'
data['decade'] = data['year'].apply(lambda x: np.floor(x / 10) * 10)

# Filter only winner from USA
usa_winner = data.loc[data['birth_country'] == 'United States of America', ['decade']]
usa_winner = usa_winner.groupby('decade').size().reset_index(name="USA_count")

# Filter winner are not from USA
total_winner = data.loc[:, ['decade']]
total_winner = total_winner.groupby('decade').size().reset_index(name="total_count")

# merge two dataframe
usa_dominance = pd.merge(usa_winner, total_winner, on='decade')

# Get 'dominance' of USA
usa_dominance['dominance'] = usa_dominance['USA_count'] / usa_dominance['total_count']

print(usa_dominance.to_string())
ax = usa_dominance.plot(x='decade', y='dominance')
ax.fill_between(usa_dominance['decade'], usa_dominance['dominance']+0.1, usa_dominance['dominance']-0.1, alpha=0.2)
ax.set(xlabel='decade', ylabel='usa_born_winner')
ax.grid()
plt.show()
