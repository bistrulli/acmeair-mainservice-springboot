#!/bin/bash

TAG="0.12"

# Build all
docker build -t rpizziol/acmeair-mainservice-springboot:$TAG .
docker build -t rpizziol/acmeair-authservice-springboot:$TAG ../acmeair-authservice-springboot
docker build -t rpizziol/acmeair-bookingservice-springboot:$TAG ../acmeair-bookingservice-springboot
docker build -t rpizziol/acmeair-customerservice-springboot:$TAG ../acmeair-customerservice-springboot
docker build -t rpizziol/acmeair-flightservice-springboot:$TAG ../acmeair-flightservice-springboot

# Push all
docker push rpizziol/acmeair-mainservice-springboot:$TAG
docker push rpizziol/acmeair-authservice-springboot:$TAG
docker push rpizziol/acmeair-bookingservice-springboot:$TAG
docker push rpizziol/acmeair-customerservice-springboot:$TAG
docker push rpizziol/acmeair-flightservice-springboot:$TAG

