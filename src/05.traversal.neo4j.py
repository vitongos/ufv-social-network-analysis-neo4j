'''
Created on Apr 5, 2016

@author: Victor
'''

from neo4jrestclient import traversals

from neo4jrestclient.client import GraphDatabase
from neo4jrestclient.query import Q
 
db = GraphDatabase('http://localhost:7474/db/data/')

home = db.node(name='Home')
neo = db.node(name='Thomas Anderson', age=29)
trinity = db.node(name='Trinity')
morpheus = db.node(name='Morpheus', rank='Captain')
cypher = db.node(name='Cypher')
agent_smith = db.node(name='Agent Smith', language='C++', version='1.0b')
architect = db.node(name='The Architect')

home.NEO_NODE(neo)
neo.KNOWS(trinity, age='3 days')
morpheus.KNOWS(trinity, age='12 years')
neo.KNOWS(morpheus)
morpheus.KNOWS(cypher, disclosure='public')
cypher.KNOWS(agent_smith, disclosure='secret', age='6 months')
agent_smith.CODED_BY(architect)
    
traversal_description = traversals.TraversalDescription()\
                .relationships('KNOWS', traversals.RelationshipDirection.OUTGOING)\
                .relationships('CODED_BY', traversals.RelationshipDirection.OUTGOING)\
                .filter(traversals.Filters.ALL_BUT_START_NODE)\
                .depthFirst()
traversal_description.max_depth(10)
traverser = traversal_description.traverse(neo)

for node in traverser.nodes:
    print node['name']    
