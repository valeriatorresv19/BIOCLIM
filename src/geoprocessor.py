import rasterio
import os
from typing import Dict, Optional

class GeoProcessor:
    def __init__(self, tif_path: str):
        """
        Inicializa el procesador con la ruta al archivo GeoTIFF.
        """
        if not os.path.exists(tif_path):
            raise FileNotFoundError(f"No se encontró el archivo: {tif_path}")
        self.tif_path = tif_path

    def get_climate_data(self, lat: float, lon: float) -> Optional[Dict[str, float]]:
        """
        Extrae los valores de tn, tx y pr para una coordenada específica.
        """
        try:
            with rasterio.open(self.tif_path) as src:
                if not (src.bounds.left <= lon <= src.bounds.right and 
                        src.bounds.bottom <= lat <= src.bounds.top):
                    return None

                row, col = src.index(lon, lat)

                data = {
                    "tn_min_temp": float(src.read(1)[row, col]),
                    "tx_max_temp": float(src.read(2)[row, col]),
                    "pr_precip": float(src.read(3)[row, col]),
                    "unit_temp": "Celsius",
                    "unit_precip": "mm"
                }
                return data

        except Exception as e:
            print(f"Error procesando coordenadas {lat}, {lon}: {e}")
            return None

if __name__ == "__main__":
    sample_tif = os.path.join('data', 'sample_ssp_2041_2060.tif')
    
    processor = GeoProcessor(sample_tif)
    
    result = processor.get_climate_data(4.95, -74.45)
    
    if result:
        print("Datos Extraídos Exitosamente")
        print(result)
    else:
        print("La coordenada está fuera de los límites del set de datos.")


