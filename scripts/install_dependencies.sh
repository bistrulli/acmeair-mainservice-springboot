#!/bin/bash 

sudo apt update
sudo apt install openjdk-17-jdk pip redis haproxy build-essential -y

sudo /etc/init.d/haproxy stop
sudo setcap CAP_NET_BIND_SERVICE=+eip /usr/sbin/haproxy