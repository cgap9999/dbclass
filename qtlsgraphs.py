import seaborn as sns
import pandas as pd

data= pd.read_csv('mediciones.csv')
sns.boxplot(data=data.ix[:,4:20])
