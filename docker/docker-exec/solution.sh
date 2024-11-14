sudo docker run -d --name jusan-docker-exec -p 8181:80 nginx:mainline
sudo docker exec -it jusan-docker-exec bash

cat /etc/nginx/conf.d/jusan-docker-exec.conf 
server {
    listen 80;
    server_name jusan.singularity;

    location / {return 200 'Hello, from jusan-docker-exec';}
    location /home {return 201 'This is my home!';}
    location /about {return 202 'I am just an exercise!';}
}

nginx -s reload
exit