import pandas as pd

orders = pd.read_csv('instacart_2017_05_01/orders.csv')
products = pd.read_csv('instacart_2017_05_01/products.csv')

print('Narudzbbina: ' orders.count() ['order_id'])
print('Korisnici: ' orders['user_id'].drop_duplicates().count())
print('Proizvodi: ' products['product_id'].count())
