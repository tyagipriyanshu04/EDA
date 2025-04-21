df.groupby('Ship Mode')['Profit'].sum().plot(kind='bar', title='Profit by Shipping Mode')
plt.ylabel('Profit')
plt.show()

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])
df['Delivery Time (Days)'] = (df['Ship Date'] - df['Order Date']).dt.days
sns.boxplot(x='Ship Mode', y='Delivery Time (Days)', data=df)
plt.title('Delivery Time by Shipping Mode')
plt.show()
