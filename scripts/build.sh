#!/bin/bash 

cd ~/git

cd acmeair-mainservice-springboot/
mvn clean package
cd ../


cd acmeair-authservice-springboot/
mvn clean package
cd ../

cd acmeair-customerservice-springboot/
mvn clean package
cd ../

cd acmeair-flightservice-springboot/
mvn clean package
cd ../

cd acmeair-bookingservice-springboot/
mvn clean package
cd ../

cd acmeair-mainservice-springboot/
mvn clean package
cd ../
