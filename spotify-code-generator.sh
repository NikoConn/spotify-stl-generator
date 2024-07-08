#!/bin/bash

# Verificar que se hayan proporcionado los argumentos necesarios
if [ $# -ne 2 ]; then
    docker run --rm spotify-code-generator 
    exit 1
fi

# Extraer los argumentos
spotify_url="$1"
output_zip="$2"

#create data
mkdir data;

# Ejecutar el contenedor Docker con los argumentos
docker run --rm -v "$(pwd)/data:/app/data" spotify-code-generator "$spotify_url" "/app/data/tmp.zip" && mv data/tmp.zip $output_zip
