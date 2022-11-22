#!/bin/bash 

set -x

sudo pkill -9 -f acmeair
sudo pkill -9 -f nginx

java -jar ~/git/acmeair-mainservice-springboot/target/acmeair-mainservice-springboot-2.1.1-SNAPSHOT.jar &
mainPid=$!

sleep 10

java -jar ~/git/acmeair-authservice-springboot/target/acmeair-authservice-springboot-2.1.1-SNAPSHOT.jar --LICENSE=accept --MONGO_HOST=localhost \
--customer.service=acmeair-nginx/customer &
authPid=$!

sleep 10

java -jar ~/git/acmeair-customerservice-springboot/target/acmeair-customerservice-springboot-2.1.1-SNAPSHOT.jar --LICENSE=accept --MONGO_HOST=localhost &
custPid=$!

sleep 10

java -jar ~/git/acmeair-bookingservice-springboot/target/acmeair-bookingservice-springboot-2.1.1-SNAPSHOT.jar --LICENSE=accept --MONGO_HOST=localhost \
--customer.service=acmeair-nginx/customer --flight.service=acmeair-nginx/flight &
bookPid=$!

sleep 10

java -jar ~/git/acmeair-flightservice-springboot/target/acmeair-flightservice-springboot-2.1.1-SNAPSHOT.jar --LICENSE=accept --MONGO_HOST=localhost &
flightPid=$!

sleep 10

sudo nginx -c  ~/git/acmeair-mainservice-springboot/nginx/conf/nginx.conf