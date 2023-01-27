#!/bin/bash 

sudo apt update
sudo apt install dirmngr gnupg apt-transport-https ca-certificates software-properties-common

wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
sudo add-apt-repository 'deb [arch=amd64] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse'

sudo apt update

 sudo apt install mongodb-org
 sudo systemctl enable --now mongod