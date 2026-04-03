
import rasterio
from rasterio.transform import from_origin
import numpy as np
import os

def create_synthetic_ssp_raster(output_path):
    """
    Genera un GeoTIFF sintético para simular escenarios SSP (2041-2060).
    Estructura de 3 bandas:
    Banda 1: tn (Temp. Mínima promedio)
    Banda 2: tx (Temp. Máxima promedio)
    Banda 3: pr (Precipitación total mensual)
    """
    print(f"--- Iniciando generación de datos sintéticos en {output_path} ---")

    # (Simulando una zona de los Andes colombianos
    # Resolución de 0.01 grados (~1km)
    width, height = 100, 100
    lon_ul, lat_ul = -74.5, 5.0  
    pixel_size = 0.01
    
    transform = from_origin(lon_ul, lat_ul, pixel_size, pixel_size)
    crs = 'EPSG:4326' 
  
    # configuracion del archivo de salida
    new_dataset = rasterio.open(
        output_path,
        'w',
        driver='GTiff',
        height=height,
        width=width,
        count=3,           
        dtype='float32',
        crs=crs,
        transform=transform,
        nodata=-9999.0
    )

    # Generación de datos con NumPy 
    np.random.seed(42) 
    
    # Banda 1: tn (Temp Mínima)
    tn = np.random.uniform(8, 18, (height, width)).astype('float32')
    
    # Banda 2: tx (Temp Máxima) 
    tx = tn + np.random.uniform(8, 15, (height, width)).astype('float32')
    
    # Banda 3: pr (precipitación) 
    pr = np.random.uniform(50, 400, (height, width)).astype('float32')

    # Escribir las bandas y asignar descripciones
    new_dataset.write(tn, 1)
    new_dataset.set_band_description(1, "Monthly Avg Min Temp (tn)")
    
    new_dataset.write(tx, 2)
    new_dataset.set_band_description(2, "Monthly Avg Max Temp (tx)")
    
    new_dataset.write(pr, 3)
    new_dataset.set_band_description(3, "Monthly Total Precipitation (pr)")

    new_dataset.close()
    print(f"--- Archivo GeoTIFF generado con éxito en: {output_path} ---")

if __name__ == "__main__":
    # Aseguramos que la carpeta data existe
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    target_file = os.path.join(data_dir, 'sample_ssp_2041_2060.tif')
    create_synthetic_ssp_raster(target_file)
