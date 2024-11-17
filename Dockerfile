FROM ubuntu:22.04

# Actualizar el sistema e instalar dependencias
RUN apt update && apt install -y python3.11 python3-pip libxrender1 libxxf86vm-dev libxfixes3 libxi6 libxkbcommon-x11-dev libsm6 libgl1

# Instalar bpy y requests usando pip
RUN pip3 install bpy==4.2.* requests

# Crear un directorio de trabajo
WORKDIR /app

# Copiar el script en el contenedor
COPY . /app

# Establecer el punto de entrada para ejecutar el script
ENTRYPOINT ["python3.11", "main.py"]