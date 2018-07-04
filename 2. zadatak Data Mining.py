
import pandas as pd
import matplotlib.pyplot as plt

orders = pd.read_csv('instacart_2017_05_01/orders.csv')
broj_narudzbina_po_korisniku = orders.groupby('user_id').count()
print(broj_narudzbina_po_korisniku.mean()['order_id'])

brpbn = broj_narudzbina_po_korisniku.groupby('order_id').count()['eval_set']
brpbn.plot()
plt.show()
