'''
Created on Apr 5, 2016

@author: Victor
'''

from neo4jrestclient.client import GraphDatabase
from neo4jrestclient.query import Q
 
db = GraphDatabase("http://localhost:7474/db/data/")

PERSON = 'Person'
 
# Crear dos nodos y una relacion del primero al segundo
firstNode = db.node( name = 'Alice', age = 25 )
secondNode = db.node( name = 'Bob', age = 30 )
knows_rel = firstNode.KNOWS(secondNode, since = 2000)

# Explorar los atributos de la relacion
print knows_rel.type, 'comienza en', knows_rel.start['name'], 'y termina en', knows_rel.end['name']

# Crear una etiqueta y asignar nodos a ella
person_label = db.labels.create(PERSON)
person_label.add(firstNode, secondNode)

# Asignar etiqueta a un nodo recien creado
thirdNode = db.node( name = 'Zach', age = 27 )
thirdNode.labels.add(PERSON)

# Filtrar nodos con una etiqueta por cierta propiedad
older_than_27 = person_label.filter(Q('age', 'gte', 27))
print 'Mayores de 27:'
for person in older_than_27:
    print person['name']
    
q = """MATCH (n) OPTIONAL MATCH (n)-[r]-() delete n, r"""
db.query(q)    
