import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_excel("/Users/priyanshutyagi/Desktop/Sample - Superstore(Dataset).xlsx")

region_profit = df.groupby('Region')['Profit'].sum().sort_values()
region_profit.plot(kind='barh', title='Profit by Region')
plt.xlabel('Total Profit')
plt.show()

top_states = df.groupby('State')['Profit'].sum().sort_values()
top_states.tail(10).plot(kind='barh', title='Top 10 States by Profit')
plt.xlabel('Profit')
plt.show()

cat_profit = df.groupby('Category')['Profit'].sum()
cat_profit.plot(kind='bar', title='Profit by Category')
plt.ylabel('Profit')
plt.show()
