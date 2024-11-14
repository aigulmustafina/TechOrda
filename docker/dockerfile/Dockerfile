FROM nginx:mainline
COPY jusan-dockerfile.conf /etc/nginx/conf.d/jusan-dockerfile.conf
RUN mkdir -p /var/www/jusan-dockerfile
COPY ./jusan-dockerfile/ /var/www/jusan-dockerfile/

EXPOSE 80