Demos y fuentes de bases de datos de grafos con Neo4j
=====================================================

Instalación
-----------

A continuación se especifica el proceso de instalación de los diferentes sistemas necesarios para ejecutar las demos.

### Instalar el repositorio clonándolo de Github:
Ejecutar el siguiente script:
```bash
sudo yum -y install git
cd
git clone https://github.com/vitongos/ufv-social-network-analysis-neo4j neo4j-src
chmod +x neo4j-src/deploy/*.sh
```

### Instalar Neo4j
Ejecutar el siguiente script:
```bash
cd ~/neo4j-src/
deploy/neo4j.sh
```

### Instalar Python
Ejecutar el siguiente script:
```bash
cd ~/neo4j-src/
deploy/python.sh
```

### Instalar Eclipse
Ejecutar el siguiente script:
```bash
cd ~/neo4j-src/
deploy/eclipse.sh
```

### Instalar PyDev
Descargar [PyDev](https://dl.bintray.com/fabioz/pydev/4.5.5/)
Instalar el PyDev en Eclipse

### Instalar Java 8
Descargar [Java 8](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)

Ejecutar el siguiente script:
```bash
cd ~/neo4j-src/
deploy/java8.sh
```
