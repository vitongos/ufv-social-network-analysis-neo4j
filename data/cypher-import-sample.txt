USING PERIODIC COMMIT 200
LOAD CSV WITH HEADERS FROM 'file:///home/cloudera/neo4j-src/data/nodes.csv' AS line 
CREATE (p:Person {id:toInt(line.id), fname:line.first_name, lname:line.last_name, email:line.email, 
gender:line.gender, city:line.city, country:line.country, born:line.born})
RETURN p;

CREATE INDEX ON :Person(id)

USING PERIODIC COMMIT 200
LOAD CSV WITH HEADERS FROM 'file:///home/cloudera/neo4j-src/data/relationships.csv' AS line
MATCH (p:Person {id:toInt(line.id1)}), (q:Person {id:toInt(line.id2)}) 
CREATE path=(p)-[:KNOWS {since:line.since}]->(q) 
RETURN path;
