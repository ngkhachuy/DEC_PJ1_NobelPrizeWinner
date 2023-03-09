import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# Read data
data = pd.read_csv('data/nobel.csv')
# Create column 'decade' from 'year'
data['decade'] = data['year'].apply(lambda x: np.floor(x / 10) * 10)
# Drop where 'sex' is n/a
data.dropna(subset=['sex'], inplace=True)

# Calculation
data['male_count'] = data['sex'] == 'Male'
data = data.groupby(['decade', 'category'], as_index=False)['male_count'].mean()
data['female_count'] = 1 - data['male_count']

print(data)

# Visualized
sns.set()
fig, ax = plt.subplots(1, 2, figsize=(15, 5))
fig.suptitle('What is the gender of a typical Nobel Prize winner?')
sns.lineplot(x=data["decade"], y=data["female_count"], hue=data["category"], ax=ax[0])
sns.lineplot(x=data["decade"], y=data["male_count"], hue=data["category"], ax=ax[1])
ax[0].set_title('Female')
ax[1].set_title('Male')
plt.show()
