'''
Created on Apr 5, 2016

@author: Victor
'''

from neo4jrestclient.client import GraphDatabase
from neo4jrestclient.query import Q
from neo4jrestclient.constants import DESC

db = GraphDatabase("http://localhost:7474/db/data/")

nodes = []

nodes.append(db.node(name = 'Robert Parsons', code=1))
nodes.append(db.node(name = 'William Gates', code=5))
nodes.append(db.node(name = 'Sergey Brin', code=2))
nodes.append(db.node(name = 'Gordon Moore', code=4))
nodes.append(db.node(name = 'Steven Paul Jobs', code=3))

lookup = Q('name', istartswith='s')
s_founders = db.nodes.filter(lookup)
print 'Comenzando con S:'
for node in s_founders:
    print '-', node['name']
    
    
lookup = Q('name', istartswith='s') & Q('name', iendswith='n')
sn_founders = db.nodes.filter(lookup)
print
print 'Comenzando con S y terminando con N:'
for node in sn_founders:
    print '-', node['name']
 
index = db.nodes.indexes.create('index')
for node in nodes:
    index.add('founders', 'none', node)
other_founders = index.filter(Q('code', 'gte', 3))
print
for node in other_founders:
    print '-', node['name']
    
print
ordered = db.nodes.filter(Q('name', 'contains', 'e')).order_by('code', DESC)
for node in ordered:
    print '-', node['name']

q = """MATCH (n) OPTIONAL MATCH (n)-[r]-() delete n, r"""
db.query(q)    
