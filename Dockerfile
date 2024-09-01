# Usa la imagen base de Python 3.11 en Alpine
FROM python:3.11-alpine

# Configura el directorio de trabajo
WORKDIR /code

# Actualiza el índice de paquetes e instala dependencias necesarias
RUN apk update && apk add --no-cache \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev \
    libpq \
    bash

# Copia el archivo de requisitos e instala las dependencias de Python
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Copia el código fuente al contenedor
COPY . /code/

# Configura la variable de entorno PYTHONPATH
ENV PYTHONPATH=/code

# Copia y establece el script de entrada
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Expon el puerto 8000 para la aplicación
EXPOSE 8000

# Usa el script de entrada para iniciar la aplicación
ENTRYPOINT ["/entrypoint.sh"]
