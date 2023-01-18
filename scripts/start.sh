#!/bin/bash 

sudo pkill -9 -f acmeair
sudo pkill -9 -f haproxy
#sudo pkill -9 -f nginx



java -jar ~/git/acmeair-mainservice-springboot/target/acmeair-mainservice-springboot-2.1.1-SNAPSHOT.jar &
sleep 10

#/login
java -jar ~/git/acmeair-authservice-springboot/target/acmeair-authservice-springboot-2.1.1-SNAPSHOT.jar --server.port=9081 \
--LICENSE=accept --customer.service=185.154.155.43/customer &
sleep 10

#/validateid
java -jar ~/git/acmeair-customerservice-springboot/target/acmeair-customerservice-springboot-2.1.1-SNAPSHOT.jar --server.port=9086 &
sleep 10

#GET /byid/{custid}
java -jar ~/git/acmeair-customerservice-springboot/target/acmeair-customerservice-springboot-2.1.1-SNAPSHOT.jar --server.port=9087 &
sleep 10

# POST /byid/{custid}
java -jar ~/git/acmeair-customerservice-springboot/target/acmeair-customerservice-springboot-2.1.1-SNAPSHOT.jar --server.port=9088 &
sleep 10

#/updateCustomerTotalMiles
java -jar ~/git/acmeair-customerservice-springboot/target/acmeair-customerservice-springboot-2.1.1-SNAPSHOT.jar --server.port=9089 &
sleep 10



#/bookflights
java -jar ~/git/acmeair-bookingservice-springboot/target/acmeair-bookingservice-springboot-2.1.1-SNAPSHOT.jar  --server.port=9082 &
sleep 10

#/bybookingnumber
java -jar ~/git/acmeair-bookingservice-springboot/target/acmeair-bookingservice-springboot-2.1.1-SNAPSHOT.jar --server.port=9083 &
sleep 10

#byuser
java -jar ~/git/acmeair-bookingservice-springboot/target/acmeair-bookingservice-springboot-2.1.1-SNAPSHOT.jar --server.port=9084 &
sleep 10

#cancelbooking
java -jar ~/git/acmeair-bookingservice-springboot/target/acmeair-bookingservice-springboot-2.1.1-SNAPSHOT.jar --server.port=9085 &
sleep 10


java -jar ~/git/acmeair-flightservice-springboot/target/acmeair-flightservice-springboot-2.1.1-SNAPSHOT.jar --server.port=9090 &
sleep 10

java -jar ~/git/acmeair-flightservice-springboot/target/acmeair-flightservice-springboot-2.1.1-SNAPSHOT.jar --server.port=9091 &
sleep 10

#sudo nginx -c  ~/git/acmeair-mainservice-springboot/nginx/conf/nginx.conf
sudo haproxy -f ~/git/acmeair-mainservice-springboot/haproxy/haproxy.cfg &
echo "startup complete"
