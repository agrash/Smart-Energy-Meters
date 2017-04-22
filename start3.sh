#!/bin/bash

cd /
cd home/pi
#python test4.py
sleep 90
rm -r data.txt
sudo chmod 666 /dev/ttyUSB0 # allow access to serial port
cat < /dev/ttyUSB0 > data.txt # used to read data from serial port
