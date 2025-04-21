df.groupby('Segment')['Order ID'].nunique().plot(kind='bar', title='Order Count by Customer Segment')
plt.ylabel('Number of Orders')
plt.show()

avg_order = df.groupby('Segment')['Sales'].mean()
avg_order.plot(kind='bar', title='Average Order Value by Segment')
plt.ylabel('Avg Sales')
plt.show()
