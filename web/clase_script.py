import requests

pedido = requests.get('https://macowins-server.herokuapp.com/prendas/400')
print(pedido)

pedidox = requests.get('https://macowins-server.herokuapp.com/prendas/400')
print(pedidox.headers)

pedido1 = requests.get('https://macowins-server.herokuapp.com/prendas/').json()
print(pedido1)

pedido2 = requests.get('https://macowins-server.herokuapp.com/prendas/').json()
print(len(pedido2))

pedido = requests.get('https://macowins-server.herokuapp.com/prendas/400')
print(pedido.status_code)

pedido3 = requests.get('https://macowins-server.herokuapp.com/prendas/1')
print(pedido3.status_code)

import ipywidgets as widgets
import jupyter as pd
import voila as juju

