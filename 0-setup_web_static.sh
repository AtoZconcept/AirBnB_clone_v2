#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
# this Install Nginx if it not already installed
sudo apt-get -y update
sudo apt-get -y install nginx

# creating directory for file to be hosted
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# create fake HTML file to test the fuctionality of the srver
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# this Create a symbolic link and deleted and recreated
# every time the script is ran.
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo sed -i '/server_name _;/a \\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-enabled/default
sudo service nginx restart
exit 0