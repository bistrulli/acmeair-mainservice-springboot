#!/bin/bash 

cd ../../

cd acmeair-ctrlmnt-springboot/
git pull
mvn clean install
cd ../

cd acmeair-mainservice-springboot/
git pull
mvn clean package
cd ../


cd acmeair-authservice-springboot/
git pull
mvn clean package
cd ../

cd acmeair-customerservice-springboot/
git pull
mvn clean package
cd ../

cd acmeair-flightservice-springboot/
git pull
mvn clean package
cd ../

cd acmeair-bookingservice-springboot/
git pull
mvn clean package
cd ../
