#!/bin/bash

cd
wget http://mirror.ibcp.fr/pub/eclipse//technology/epp/downloads/release/mars/2/eclipse-java-mars-2-linux-gtk-x86_64.tar.gz
sudo mv eclipse-java-mars-2-linux-gtk-x86_64.tar.gz /opt/
cd /opt
sudo tar xzf eclipse-java-mars-2-linux-gtk-x86_64.tar.gz
sudo chown cloudera:cloudera eclipse -R
sudo ln -s /opt/eclipse/eclipse /usr/bin/eclipse
