import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('df1', index_col=0)
print(df1.head())

df2 = pd.read_csv('df2')
print(df2.head())

# making histogram with pandas
df1['A'].hist(bins=30)
plt.show()

# pandas built in plot types
df1['A'].plot(kind='hist', bins=30)
plt.show()
# another way
df1['A'].plot.hist()
plt.show()

# other plot types. `areaplot`
df2.plot.area(alpha=0.4)
plt.show()

# barplot
df2.plot.bar(stacked=True)
plt.show()

# scatter plot
df1.plot.scatter(x='A', y='B', c='C', cmap='coolwarm')
plt.show()

# making dataframe
df = pd.DataFrame(np.random.randn(1000, 2), columns=['a', 'b'])
# hexplot
df.plot.hexbin(x='a', y='b', gridsize=25)
plt.show()

# kernel density estimation
df2.plot.kde()
plt.show()