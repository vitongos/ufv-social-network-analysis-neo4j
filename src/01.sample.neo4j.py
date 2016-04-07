'''
Created on Apr 5, 2016

@author: Victor
'''

from neo4jrestclient.client import GraphDatabase
 
db = GraphDatabase("http://localhost:7474/db/data/")

KNOWS = 'KNOWS'
 
firstNode = db.nodes.create( name = 'Alice' )
secondNode = db.nodes.create( name = 'Bob' )
knows_rel = firstNode.relationships.create(KNOWS, secondNode, since = 1980)

print firstNode.get('name'), 'knows', secondNode.get('name'), 'since', knows_rel.get('since')

print 'Node', firstNode.id, 'knows', 'Node', secondNode.id, 'since', knows_rel.get('since')

q = """MATCH (n) OPTIONAL MATCH (n)-[r]-() delete n, r"""
db.query(q)    
