items = set()
for col in df:
    items.update(df[col].unique())
print(items)
Out:
{'Bread', 'Cheese', 'Meat', 'Eggs', 'Wine', 'Bagel', 'Pencil',
       'Diaper', 'Milk']}
