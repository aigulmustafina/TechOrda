#!/bin/bash

CONTAINER_NAME="local-vps-22"
IMAGE_NAME="atlekbai/local-vps"

if [ "$(docker ps -q -f name=$CONTAINER_NAME)" ]; then
  echo "Контейнер $CONTAINER_NAME уже запущен."
else
  docker run -d --name $CONTAINER_NAME -p 2222:22 -p 80:80 $IMAGE_NAME
  echo "Контейнер $CONTAINER_NAME запущен."
fi

if [ ! -f ~/.ssh/id_rsa ]; then
  ssh-keygen -t rsa -b 2048 -N "" -f ~/.ssh/id_rsa
  echo "SSH-ключ создан."
fi


docker exec -it $CONTAINER_NAME mkdir -p /root/.ssh
docker cp ~/.ssh/id_rsa.pub $CONTAINER_NAME:/root/.ssh/authorized_keys
docker exec -it $CONTAINER_NAME chmod 600 /root/.ssh/authorized_keys
docker exec -it $CONTAINER_NAME chmod 700 /root/.ssh

echo "SSH-ключ установлен в контейнер."
