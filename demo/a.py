import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Read data
nobel = pd.read_csv('../data/nobel.csv')

#3. USA dominance
# Calculating the proportion of USA born winners per decade
nobel['usa_born_winner'] = nobel['birth_country']=='United States of America'
nobel['decade'] = (np.floor(nobel['year']/10)*10).astype(int)
prop_usa_winners = nobel.groupby(['decade'], as_index=False)['usa_born_winner'].mean()

# Display the proportions of USA born winners per decade
# display(prop_usa_winners)

#=============================================
#4. USA dominance, visualized
# Setting the plotting theme
import seaborn as sns
sns.set()
# and setting the size of all plots.
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [11, 7]

# Plotting USA born winners
ax = sns.lineplot(x='decade', y='usa_born_winner', data=nobel)

# Adding %-formatting to the y-axis
from matplotlib.ticker import PercentFormatter
ax.yaxis.set_major_formatter(PercentFormatter(1.0))
plt.show()
