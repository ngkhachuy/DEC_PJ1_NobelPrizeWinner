import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read data
data = pd.read_csv('data/nobel.csv')
# Drop row have None(N/a) on column 'birth_date'
data.dropna(subset=['birth_date'], inplace=True)

# Create column 'year_old'
data['year_old'] = data['year'] - pd.to_numeric(data['birth_date'].transform(lambda x: str(x)[0:4]))

data = data.loc[:, ['year', 'year_old', 'category']]

# Visualized
# Setting the plotting theme
sns.set()
# and setting the size of all plots.
plt.rcParams['figure.figsize'] = [11, 7]
g = sns.relplot(data=data, x="year", y="year_old", row="category")
g.set_axis_labels("year_old", "year")
plt.show()
