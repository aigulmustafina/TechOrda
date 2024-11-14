curl -o nginx.conf https://raw.githubusercontent.com/Smagicom/TechOrda/main/docker/docker-bind/nginx.conf

sudo docker run -d \
  -p 7777:80 \
  --name jusan-docker-bind \
  -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf \
  nginx:mainline
