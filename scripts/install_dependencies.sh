#!/bin/bash 

sudo apt update
sudo apt install openjdk-17-jdk pip redis haproxy build-essential -y

sudo /etc/init.d/haproxy stop
sudo setcap CAP_NET_BIND_SERVICE=+eip /usr/sbin/haproxy

git config --global user.email 183048+bistrulli@users.noreply.github.com
git config --global user.name  EMI