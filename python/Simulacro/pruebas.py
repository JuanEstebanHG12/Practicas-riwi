lista = [
    {
    'name' : "prueba",
    'brand' : "brand test",
    'category': "category test",
    'price' : 1,
    'amount' : 2,
    'warranty' : 3
    },
    {
    'name' : "prueba2",
    'brand' : "brand test",
    'category': "category test",
    'price' : 2,
    'amount' : 2,
    'warranty' : 3
    },
    {
    'name' : "prueba3",
    'brand' : "brand test",
    'category': "category test",
    'price' : 5,
    'amount' : 2,
    'warranty' : 3
    },
    {
    'name' : "prueba3",
    'brand' : "nada",
    'category': "category test",
    'price' : 10,
    'amount' : 2,
    'warranty' : 3
    },
    {
    'name' : "prueba3",
    'brand' : "brand test",
    'category': "category test",
    'price' : 4,
    'amount' : 2,
    'warranty' : 3
    },
]

def top_tres(lista):
    nueva = sorted(lista, key= lambda x : x['price'])
    return nueva

def por_marcas(lista):
    nueva = list(filter(lambda x : x['brand']== 'nada',lista))
    return nueva
    
""" nuevas = top_tres(lista)
nuevas.reverse()
for p in range(0,3):
   print( nuevas[p]['price']) """
   
filtrados = por_marcas(lista)
for p in filtrados:
    print(f"Nombre {p['name']}")
    print(f"brand {p['brand']}")