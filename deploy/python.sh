#!/bin/bash

cd ~/Downloads
wget http://www.python.org/ftp/python/2.7.6/Python-2.7.6.tgz
tar xfv Python-2.7.6.tgz
rm -rf Python-2.7.6.tgz
cd Python-2.7.6
./configure --prefix=/usr/local
make
make altinstall
export PATH="/usr/local/bin:$PATH"
cd ~/Downloads
wget --no-check-certificate https://pypi.python.org/packages/source/s/setuptools/setuptools-1.4.2.tar.gz
tar xvf setuptools-1.4.2.tar.gz
rm -rf setuptools-1.4.2.tar.gz
cd setuptools-1.4.2
curl https://bootstrap.pypa.io/get-pip.py | python2.7
pip install virtualenv
pip install neo4jrestclient

