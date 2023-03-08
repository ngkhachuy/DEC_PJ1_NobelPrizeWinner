import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv('data/nobel.csv')
data['decade'] = data['year'].apply(lambda x: np.floor(x / 10) * 10)
data.dropna(subset=['sex'], inplace=True)

total_category = data.loc[:, ['decade', 'category']]
total_category = data.groupby(['decade', 'category']).size().reset_index(name='total_count')

gender_count_category = data.loc[:, ['decade', 'category', 'sex']]
gender_count_category = data.groupby(['decade', 'category', 'sex']).size().reset_index(name='gender_count')

category = pd.merge(gender_count_category, total_category, on=['decade', 'category'])
category['percent'] = category['gender_count'] / category['total_count']

female_total = category.loc[category['sex'] == 'Female', ['decade', 'category', 'percent']]
male_total = category.loc[category['sex'] == 'Male', ['decade', 'category', 'percent']]

female_total = female_total.pivot(index='decade', columns='category', values='percent')
male_total = male_total.pivot(index='decade', columns='category', values='percent')

female_total.fillna(0, inplace=True)
male_total.fillna(0, inplace=True)

print(female_total)
print(male_total)

fig, ax = plt.subplots(nrows=2, ncols=1)
fig.set_figheight(10)
fig.set_figwidth(10)

ax[0].plot()
ax[1].plot()

ax_female = female_total.plot(ax=ax[0])
ax_male = male_total.plot(ax=ax[1])

ax_female.set(xlabel='decade', ylabel='female_winner')
ax_male.set(xlabel='decade', ylabel='male_winner')

plt.show()
