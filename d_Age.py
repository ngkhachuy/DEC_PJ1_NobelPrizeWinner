import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# Read data
data = pd.read_csv('data/nobel.csv')
# Drop row have None(N/a) on column 'birth_date'
data.dropna(subset=['birth_date'], inplace=True)
# Create column 'year_old'
data['year_old'] = data['year'] - pd.to_numeric(data['birth_date'].transform(lambda x: str(x)[0:4]))
data = data.loc[:, ['year', 'year_old']]

# Visualized
# Setting the plotting theme
sns.set()

g = sns.lmplot(data=data, x="year", y="year_old")
g.set_axis_labels("year", "year_old")

plt.show()
