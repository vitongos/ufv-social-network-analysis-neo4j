install.packages("RNeo4j")
library(igraph)
library(RNeo4j)

#
# 1. Conectar a la Base de datos.
#
graph <- startGraph("http://localhost:7474/db/data/")

query <- "MATCH (p:Person {id:{id}}) RETURN p"

from <- getSingleNode(graph, query, id = 1)

to <- getSingleNode(graph, query, id = 2977)

p <- shortestPath(from, "KNOWS", to, max_depth = 10)
n <- nodes(p)
sapply(n, function(x) x$lname)

#
# 2. Crear un igraph
#
query <- "MATCH (n)-->(m) RETURN n.fname, m.fname LIMIT 25"

edgelist <- cypher(graph, query)
g <- graph.data.frame(edgelist, directed = F)
g

# Mostrar el grafo
plot(g, edge.color='Black',vertex.size=10)

