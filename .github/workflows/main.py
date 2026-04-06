import subprocess
import sys
import os
import time

def run_workflow():
    """
    Orquestador principal del proyecto:
    1. Genera los datos sintéticos (si no existen o para refrescar).
    2. Inicia el servidor de la API.
    """
    print("Workflow: Climate-Bio-Bridge")
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_file = os.path.join(base_dir, 'data', 'sample_ssp_2041_2060.tif')
    generator_script = os.path.join(base_dir, 'scripts', 'generate_sample_ssp.py')

    if not os.path.exists(data_file):
        print("Datos no detectados. Ejecutando generador de GeoTIFF...")
        try:
            subprocess.run([sys.executable, generator_script], check=True)
            print("Datos sintéticos generados correctamente.")
        except subprocess.CalledProcessError as e:
            print(f"Error al generar los datos: {e}")
            sys.exit(1)
    else:
        print("El archivo de datos ya existe. Saltando generación...")

    print("Iniciando servidor FastAPI con Uvicorn...")
    time.sleep(1) 
    
    try:
        subprocess.run([
            "uvicorn", "src.api:app", 
            "--host", "0.0.0.0", 
            "--port", "8000"
        ], check=True)
    except KeyboardInterrupt:
        print("\n Servidor detenido por el usuario.")
    except Exception as e:
        print(f" Error al iniciar la API: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_workflow()
