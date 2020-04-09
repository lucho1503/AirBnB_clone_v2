# sets my servers to deployment

exec {'install nginx':
  command => 'sudo apt-get -y update && sudo apt-get -y install nginx && sudo mkdir -p /data/web_static/releases/test/ && sudo mkdir -p /data/web_static/shared/ && echo "<html></html>" > /data/web_static/releases/test/index.html && ln -sf /data/web_static/releases/test/ /data/web_static/current && chown -R ubuntu:ubuntu /data/ && sudo sed -i "38i\ \tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n" /etc/nginx/sites-enabled/default && sudo service nginx restart && exit 0',
  provider => shell,
}
