#!/bin/bash 

cd 
wget https://dlcdn.apache.org/maven/maven-3/3.8.7/binaries/apache-maven-3.8.7-bin.tar.gz
tar -xvf apache-maven-3.8.7-bin.tar.gz

echo export 'JAVA_HOME=/lib/jvm/java-17-openjdk-amd64/' >> .profile
echo 'export M2_HOME=~/apache-maven-3.8.7' >> .profile
echo 'export MAVEN_HOME=~/apache-maven-3.8.7' >> .profile
echo 'export PATH=${M2_HOME}/bin:${PATH}' >> .profile

source .profile