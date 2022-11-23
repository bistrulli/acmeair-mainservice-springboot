#!/bin/bash 

cd ../../

cd acmeair-mainservice-springboot/
git add -A
git commit -m "$1"
git push
cd ../


cd acmeair-authservice-springboot/
git add . -A
git commit -m "$1"
git push
cd ../

cd acmeair-customerservice-springboot/
git add . -A
git commit -m "$1"
git push
cd ../

cd acmeair-flightservice-springboot/
git add . -A
git commit -m "$1"
git push
cd ../

cd acmeair-bookingservice-springboot/
git add . -A
git commit -m "$1"
git push
cd ../

cd acmeair-mainservice-springboot/
git add . -A
git commit -m "$1"
git push
cd ../
