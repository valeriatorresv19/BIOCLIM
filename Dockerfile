FROM python:3.11-slim

#dependencias del sistema necesarias para mapas y TIFs (GDAL)
RUN apt-get update && apt-get install -y \
    binutils \
    libgdal-dev \
    g++ \
    && rm -rf /var/lib/apt/lists/*

#variables de entorno para que Python encuentre GDAL
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

WORKDIR /app

# requerimientos primero (para aprovechar el caché)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000

# arrancar el servidor automáticamente
CMD ["python", "workflows/main.py"]
