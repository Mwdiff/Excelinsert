from DBcm import UseDatabase
import matplotlib.pyplot as plt
from init import dbconfig


def SelectHistory(sku: str) -> 'rows':
    with UseDatabase(dbconfig) as cursor:
        _SQL = """SELECT * FROM phistory WHERE symbol=%s ORDER BY Data""" % sku
        cursor.execute(_SQL)
        return cursor.fetchall()

x = []
y = []

sku = input('Podaj sku produktu: ')

data = SelectHistory(sku)

for row in data:
    x.append(row[1])
    y.append(row[0])

plt.plot(x, y)
plt.show()