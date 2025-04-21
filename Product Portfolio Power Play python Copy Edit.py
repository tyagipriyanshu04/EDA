subcat = df.groupby('Sub-Category')[['Sales', 'Profit']].sum().sort_values('Sales', ascending=False)
subcat.plot(kind='bar', figsize=(12, 6), title='Sales and Profit by Sub-Category')
plt.ylabel('Amount')
plt.show()
