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

