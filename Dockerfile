FROM ubuntu:22.04

# Actualizar el sistema e instalar dependencias
RUN apt update && apt install -y python3.10 python3-pip libxrender1 libxxf86vm-dev libxfixes3 libxi6 libxkbcommon-x11-dev libsm6 libgl1

# Instalar bpy y requests usando pip
RUN pip3 install bpy requests

# Crear un directorio de trabajo
WORKDIR /app

# Copiar el script en el contenedor
COPY . /app

# Establecer el punto de entrada para ejecutar el script
ENTRYPOINT ["python3.10", "main.py"]