from fastapi import FastAPI, HTTPException, Query
from src.geoprocessor import GeoProcessor
import os

app = FastAPI(
    title="Bio-Climate Insights API",
    description="API para la consulta de escenarios climáticos SSP (2041-2060) en Colombia.",
    version="1.0.0"
)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TIF_PATH = os.path.join(BASE_DIR, 'data', 'sample_ssp_2041_2060.tif')

processor = GeoProcessor(TIF_PATH)

@app.get("/")
def home():
    """Ruta de bienvenida y verificación de estado."""
    return {
        "message": "Bienvenido a la Bio-Climate Insights API",
        "status": "online",
        "data_source": "Synthetic SSP 2041-2060 (Based on Bioclim)",
        "docs": "/docs"
    }

@app.get("/climate")
def get_climate_by_coords(
    lat: float = Query(..., description="Latitud en formato decimal (WGS84)", example=4.95),
    lon: float = Query(..., description="Longitud en formato decimal (WGS84)", example=-74.45)
):
    """
    Endpoint principal: Retorna datos de temperatura y precipitación para una coordenada.
    """
    # Usamos nuestra lógica de geoprocessor.py
    result = processor.get_climate_data(lat, lon)
    
    if not result:
        raise HTTPException(
            status_code=404, 
            detail="Las coordenadas proporcionadas están fuera del área de cobertura del dataset."
        )
    
    return {
        "request": {"lat": lat, "lon": lon},
        "climate_data": result
    }

# Para correr localmente sin Docker: uvicorn src.api:app --reload
