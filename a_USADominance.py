import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.ticker import PercentFormatter

# Read data
data = pd.read_csv('data/nobel.csv')
# Create column 'decade' from 'year'
data['decade'] = data['year'].apply(lambda x: np.floor(x / 10) * 10).astype(int)
# Create column 'usa_birth' from 'birth_country'
data['usa'] = data['birth_country'] == 'United States of America'
data['total'] = 1

# Calculate %
df = data.groupby(['decade'], as_index=False)['usa', 'total'].sum()
df['percent'] = data['usa'] / data['total']
df = pd.melt(df, id_vars=['decade'], value_vars=['usa', 'total'], var_name='where', value_name='count')

sns.set()
fig, ax = plt.subplots(1, 2, figsize=(18, 7))
fig.suptitle('USA dominance')
plt.rcParams['figure.figsize'] = [11, 7]
sns.lineplot(x='decade', y='usa', data=data, ax=ax[0])
sns.barplot(x='decade', y='count', hue='where', data=df, ax=ax[1])
ax[0].yaxis.set_major_formatter(PercentFormatter(1.0))
plt.show()
