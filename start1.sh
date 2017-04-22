#!/bin/bash

# this script is used to send the ip of the pi to baadal server incase you need to ssh into the pi

sleep 4
sudo service ssh restart
sleep 60 	# to give pi sufficient time to connect to wifi before using scp
ifconfig > ip.txt
sleep 5
scp -r ~/ip.txt baadalvm@10.17.50.24:~/
sleep 4