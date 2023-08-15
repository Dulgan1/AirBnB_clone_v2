#!/usr/bin/env bash
# Script to install nginx and configure static contents directories.
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test/
sudo echo "\
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/

CONFIG="\n\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t\tautoindex off;\n\t}"
sudo sed -i "s/hbnb_static/hbnb_static$RANDOM/" /etc/nginx/sites-available/default
sudo sed -i "64i\\$CONFIG" /etc/nginx/sites-available/default
service nginx restart
