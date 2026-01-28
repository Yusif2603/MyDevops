#!/bin/bash
apt-get update
apt-get install -y docker.io
systemctl start docker
systemctl enable docker

docker network create web_network

docker run -d --name app-server --network web_network nginx
docker exec app-server sh -c "echo '<h1>Eto vnutrennee prilozhenie Yusifa!</h1>' > /usr/share/nginx/html/index.html"

sleep 60

sudo docker run -d -p 80:80 --name app-server -v /home/ubuntu/my-website:/usr/share/nginx/html nginx
