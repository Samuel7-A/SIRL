# =====================================================
# SIRL - Sistema Inteligente de Recomendación de Libros
# Archivo: utils/lector_datos.py
# Descripción: Funciones para leer y escribir archivos JSON
# =====================================================

import json
import os

def leer_preferencias(ruta: str) -> dict:
    """
    Lee el archivo JSON de preferencias del usuario generado por Scala.
    Retorna un diccionario con: nombre, genero_favorito, autor_favorito
    """
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"No se encontró el archivo: {ruta}")
    
    with open(ruta, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
    
    print(f"[Python] Preferencias leídas: {datos}")
    return datos


def guardar_recomendaciones(ruta: str, recomendaciones: list) -> None:
    """
    Guarda la lista de libros recomendados en un archivo JSON.
    Cada libro es un diccionario con: titulo, genero, autor
    """
    # Crear el directorio de salida si no existe
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(recomendaciones, archivo, ensure_ascii=False, indent=2)
    
    print(f"[Python] Recomendaciones guardadas en: {ruta}")
