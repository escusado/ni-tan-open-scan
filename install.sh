#!/bin/bash
# Install pi os and update it
# optional add the line ip=192.168.0.1 to the cmdline.txt to set the eth0

# Installing i2c Kernel Support (with Raspi-Config)
# https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c

sudo pip3 install adafruit-circuitpython-seesaw
sudo apt-get install python3-smbus
sudo apt-get install -y i2c-tools
sudo pip3 install adafruit-circuitpython-ssd1306
sudo apt-get install python3-pil

sudo sed '$ i\sudo python3 /app/index.py &' /etc/rc.local