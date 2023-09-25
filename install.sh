#!/bin/bash
# Install pi os and update it
# optional add the line ip=192.168.0.1 to the cmdline.txt to set the eth0

# Installing i2c Kernel Support (with Raspi-Config)
# https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c

sudo localedef -i en_US -f UTF-8 en_US.UTF-8
sudo apt-get install -y python3-smbus i2c-tools python3-pil python3-picamera2
sudo pip3 install adafruit-circuitpython-seesaw
sudo pip3 install adafruit-circuitpython-ssd1306
sudo chmod +x /app/start_app.sh

wget -O install_pivariety_pkgs.sh https://github.com/ArduCAM/Arducam-Pivariety-V4L2-Driver/releases/download/install_script/install_pivariety_pkgs.sh
chmod +rwx install_pivariety_pkgs.sh
./install_pivariety_pkgs.sh -p libcamera_dev
./install_pivariety_pkgs.sh -p libcamera_apps
./install_pivariety_pkgs.sh -p imx519_kernel_driver

# app and webserver on boot
sudo sed -i '$ i\sudo /app/start_app.sh &' /etc/rc.local

# open Chrome app on ui start
sudo sed -i '$a\@xset s off\n@xset -dpms\n@xset s noblank\n@chromium-browser http://localhost:8000/' /etc/xdg/lxsession/LXDE-pi/autostart
