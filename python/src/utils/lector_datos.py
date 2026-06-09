# =====================================================
# SIRL - Sistema Inteligente de Recomendación de Libros
# Archivo: utils/lector_datos.py
# Rol: Utilidades para leer/escribir JSON.
#      Exportar resultados a archivos .json en data/
# =====================================================

import json
import os
from datetime import datetime

def leer_preferencias(ruta: str) -> dict:
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"Archivo no encontrado: {ruta}")
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_json(ruta: str, datos: dict) -> None:
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)
    print(f"[JSON] Exportado a: {ruta}")

def exportar_resultado(ruta_salida: str, operacion: str, datos: dict) -> str:
    """
    Exporta cualquier resultado del menú a un archivo JSON con timestamp.
    Retorna la ruta del archivo generado.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f"{operacion}_{timestamp}.json"
    ruta_completa  = os.path.join(ruta_salida, nombre_archivo)
    os.makedirs(ruta_salida, exist_ok=True)

    envoltorio = {
        "sistema":   "SIRL - Sistema Inteligente de Recomendacion de Libros",
        "operacion": operacion,
        "timestamp": datetime.now().isoformat(),
        "resultado": datos
    }
    with open(ruta_completa, "w", encoding="utf-8") as f:
        json.dump(envoltorio, f, ensure_ascii=False, indent=2)

    return ruta_completa
