#!/bin/bash
apt-get update
apt-get install -y docker.io
systemctl start docker
systemctl enable docker

docker network create web_network

docker run -d --name app-server --network web_network nginx
docker exec app-server sh -c "echo '<h1>Eto vnutrennee prilozhenie Yusifa!</h1>' > /usr/share/nginx/html/index.html"

docker run -d --name proxy-server --network web_network -p 80:80 nginx
