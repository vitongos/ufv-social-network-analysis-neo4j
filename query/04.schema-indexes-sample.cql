MATCH (a {name:'Henry Fonda'})-[:ACTS_IN]-(m) RETURN m.title

CREATE INDEX ON :Actor(name)

MATCH (a:Actor {name:'Henry Fonda'})-[:ACTS_IN]-(m) RETURN m.title
