'''
Created on Apr 5, 2016

@author: Victor
'''

from neo4jrestclient.client import GraphDatabase
 
db = GraphDatabase('http://localhost:7474/db/data/')

index1 =  db.nodes.indexes.create('index1')

firstNode = db.node(name='Madrid', country='Spain')

secondNode = db.node(name='Zaragoza', country='Spain')

index1['places']['madrid'] = firstNode

index1['places']['zaragoza'] = secondNode

for node in index1.query('places', '?a*'):
    print node['name']
    
index1.delete('places', None, firstNode)

index1.delete('places', 'zaragoza', secondNode)

for node in index1.query('places', '*'):
    print node['name']
    
index1.delete()

q = """MATCH (n) OPTIONAL MATCH (n)-[r]-() delete n, r"""
db.query(q)    


