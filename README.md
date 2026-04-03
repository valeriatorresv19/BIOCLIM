# BIOCLIM
# 🌍 Bio-Climate Bridge: SSP Scenario Processor

### *Integración de Datos de Biodiversidad y Modelado Climático Proyectado (2041-2060)*

Este proyecto es una solución de **Backend e Informática de la Biodiversidad** diseñada para cerrar la brecha entre los datos crudos de monitoreo (inspirado en sistemas como SIVREN) y los modelos de cambio climático global (Bioclim/WorldClim). 

Desarrollado con un enfoque híbrido de **Ingeniería Biomédica y Ciencia de Datos**, este sistema permite consultar la viabilidad climática de ecosistemas bajo escenarios **SSP (Shared Socioeconomic Pathways)** mediante una API de alto rendimiento. Se usa data sintetica para probar el código.

---

##Arquitectura y Workflow

El sistema opera bajo un flujo de trabajo automatizado y contenedorizado para garantizar la reproducibilidad científica:

1.  **Data Orchestration:** Generación de capas sintéticas GeoTIFF que replican la estructura de datos climáticos de alta resolución (3 bandas: Temp Min, Temp Max, Precipitación).
2.  **Geospatial Engine:** Procesador basado en `rasterio` que realiza indexación espacial para extraer métricas climáticas precisas a partir de coordenadas geográficas.
3.  **Rest API:** Interfaz desarrollada en `FastAPI` que expone los datos procesados para su consumo en modelos de nicho ecológico o herramientas de toma de decisiones.

---

##Características Principales

* **Manejo de GeoTIFFs:** Lectura eficiente de archivos raster multibanda.
* **Escenarios Futuros:** Preparado para procesar proyecciones climáticas 2041-2060.
* **Docker Ready:** Configuración completa para despliegue inmediato, gestionando dependencias complejas como GDAL.
* **Calidad de Datos:** Validación estricta de entradas geográficas mediante `Pydantic`.

---

##Instalación y Uso

### Requisitos previos
* Docker y Docker Compose (Recomendado)
* Python 3.11+ (Si se ejecuta localmente)

### Ejecución rápida (Docker)
```bash
docker build -t bio-climate-api .
docker run -p 8000:8000 bio-climate-api
