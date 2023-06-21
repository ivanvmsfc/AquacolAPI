#!/bin/bash

# Para y elimina el conenedor de la API y el de Daemon Aemet y sus imagenes correspondientes
# Luego levanta de nuevo los contenedores

# Obtener el nombre de la imagen asociada a los contenedores
image_name1=$(sudo docker inspect -f '{{.Config.Image}}' aquacolbackend-app-1)
image_name2=$(sudo docker inspect -f '{{.Config.Image}}' aquacolbackend-db-1)

# Detener el contenedor de Docker
sudo docker stop aquacolbackend-app-1 aquacolbackend-db-1

# Eliminar el contenedor de Docker
sudo docker rm aquacolbackend-app-1 aquacolbackend-db-1

# Eliminar la imagen asociada al contenedor
sudo docker rmi "$image_name1" "$image_name2"

# Ejecutar el comando "docker-compose up"
sudo docker compose up
