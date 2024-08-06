FROM python:3.11-slim

# Actualizar paquetes e instalar dependencias
RUN apt update && apt install -y python3 python3-pip python-is-python3 git wget unzip libgl1-mesa-glx numactl \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

# Instalar Jupyter Labs y herramientas adicionales
RUN pip3 install jupyterlab jupyter ipywidgets ipykernel

# Instalar utilidades adicionales
RUN pip3 install flask tensorflow pillow

# Crear el directorio de trabajo
WORKDIR /workspaces/Plant-Disease-Classifier-RESTService

# Exponer el puerto 5000 para Flask
#EXPOSE 5000