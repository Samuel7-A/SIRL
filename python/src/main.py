# =====================================================
# SIRL - Sistema Inteligente de Recomendación de Libros
# Archivo: python/src/main.py
# Descripción: Script principal del módulo Python.
#              Lee preferencias de Scala, consulta Prolog,
#              y guarda los resultados para que Scala los lea.
# =====================================================

import sys
import os

# Agregar la carpeta src al path para importar módulos locales
sys.path.insert(0, os.path.dirname(__file__))

from utils.lector_datos import leer_preferencias, guardar_recomendaciones
from integracion.puente_prolog import PuenteProlog

def main():
    print("[Python] Iniciando módulo de integración SIRL...")

    # -------------------------------------------------------
    # Rutas de archivos (relativas a la raíz del proyecto)
    # -------------------------------------------------------
    ruta_base       = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
    ruta_prolog     = os.path.join(ruta_base, "prolog")
    ruta_entrada    = os.path.join(ruta_base, "data", "entrada", "preferencias.json")
    ruta_salida     = os.path.join(ruta_base, "data", "salida", "recomendaciones.json")

    # -------------------------------------------------------
    # PASO 1: Leer preferencias escritas por Scala
    # -------------------------------------------------------
    try:
        preferencias = leer_preferencias(ruta_entrada)
    except FileNotFoundError as e:
        print(f"[Python] Error: {e}")
        sys.exit(1)

    genero = preferencias.get("genero_favorito", "programacion")
    autor  = preferencias.get("autor_favorito", "ninguno")
    nombre = preferencias.get("nombre", "Usuario")

    print(f"[Python] Procesando recomendaciones para: {nombre}")

    # -------------------------------------------------------
    # PASO 2: Conectar con Prolog y obtener recomendaciones
    # -------------------------------------------------------
    try:
        puente = PuenteProlog(ruta_prolog)
        recomendaciones = puente.obtener_recomendaciones(genero, autor)
    except Exception as e:
        print(f"[Python] Error al consultar Prolog: {e}")
        print("[Python] Asegúrate de tener SWI-Prolog y pyswip instalados.")
        sys.exit(1)

    # -------------------------------------------------------
    # PASO 3: Guardar resultados en JSON para que Scala los lea
    # -------------------------------------------------------
    guardar_recomendaciones(ruta_salida, recomendaciones)
    print(f"[Python] Proceso completado. {len(recomendaciones)} libros recomendados.")


if __name__ == "__main__":
    main()
