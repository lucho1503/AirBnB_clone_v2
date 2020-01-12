#!/usr/bin/env bash
# this script configures a new server for the deplyment od web static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Holbertons School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sudo sed -i "38i\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/\
;\n\t\tautoindex off ; \n\t}\n" /etc/nginx/sites-available/default
sudo service nginx restart
exit 0
