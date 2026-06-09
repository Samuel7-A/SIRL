# =====================================================
# SIRL - Sistema Inteligente de Recomendación de Libros
# Archivo: python/src/main.py
# Rol de Python: MENÚ e INTEGRACIÓN.
#   Python coordina la interacción con el usuario,
#   invoca a Prolog para la lógica, y exporta JSON.
#   Puede ser llamado por Scala o ejecutarse solo.
#
# MODOS DE USO:
#   1. Modo menú interactivo:   python src/main.py
#   2. Modo API desde Scala:    python src/main.py --modo api
# =====================================================

import sys
import os
import json
import argparse

sys.path.insert(0, os.path.dirname(__file__))

from integracion.puente_prolog import PuenteProlog
from utils.lector_datos        import exportar_resultado, leer_preferencias

# Rutas base del proyecto
BASE          = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
RUTA_PROLOG   = os.path.join(BASE, "prolog")
RUTA_SALIDA   = os.path.join(BASE, "data", "salida")
RUTA_ENTRADA  = os.path.join(BASE, "data", "entrada", "preferencias.json")


def mostrar_menu():
    print("\n" + "=" * 40)
    print("  SIRL - Recomendador de Libros")
    print("=" * 40)
    print("  1. Buscar libro por titulo")
    print("  2. Buscar libros por autor")
    print("  3. Buscar libros por genero")
    print("  4. Ver generos disponibles")
    print("  5. Ver autores disponibles")
    print("  6. Obtener recomendaciones")
    print("  7. Estadisticas del sistema")
    print("  8. Exportar ultimo resultado a JSON")
    print("  9. Salir")
    print("=" * 40)


def modo_menu(puente: PuenteProlog):
    """Modo interactivo con menú para demostración."""
    ultimo_resultado = None
    ultima_operacion = "resultado"

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion (1-9): ").strip()

        if opcion == "1":
            titulo = input("Titulo del libro: ").strip()
            resultado = puente.buscar_por_titulo(titulo)
            print("\n" + json.dumps(resultado, ensure_ascii=False, indent=2))
            ultimo_resultado = resultado
            ultima_operacion = "busqueda_titulo"

        elif opcion == "2":
            autor = input("Nombre del autor: ").strip().lower()
            resultado = puente.buscar_por_autor(autor)
            print("\n" + json.dumps(resultado, ensure_ascii=False, indent=2))
            ultimo_resultado = resultado
            ultima_operacion = "busqueda_autor"

        elif opcion == "3":
            genero = input("Genero: ").strip().lower()
            resultado = puente.buscar_por_genero(genero)
            print("\n" + json.dumps(resultado, ensure_ascii=False, indent=2))
            ultimo_resultado = resultado
            ultima_operacion = "busqueda_genero"

        elif opcion == "4":
            resultado = puente.generos_disponibles()
            print("\n" + json.dumps(resultado, ensure_ascii=False, indent=2))
            ultimo_resultado = resultado
            ultima_operacion = "generos_disponibles"

        elif opcion == "5":
            resultado = puente.autores_disponibles()
            print("\n" + json.dumps(resultado, ensure_ascii=False, indent=2))
            ultimo_resultado = resultado
            ultima_operacion = "autores_disponibles"

        elif opcion == "6":
            print("Generos disponibles: ciencia_ficcion, terror, fantasia,")
            print("  distopia, programacion, algoritmos, historia, ciencia, clasico")
            genero = input("Tu genero favorito: ").strip().lower()
            autor  = input("Tu autor favorito (Enter para omitir): ").strip().lower()
            if not autor:
                autor = "ninguno"
            resultado = puente.obtener_recomendaciones(genero, autor)
            print("\n" + json.dumps(resultado, ensure_ascii=False, indent=2))
            ultimo_resultado = resultado
            ultima_operacion = "recomendaciones"

        elif opcion == "7":
            resultado = puente.obtener_estadisticas()
            print("\n" + json.dumps(resultado, ensure_ascii=False, indent=2))
            ultimo_resultado = resultado
            ultima_operacion = "estadisticas"

        elif opcion == "8":
            if ultimo_resultado is None:
                print("[!] No hay resultado para exportar. Realiza primero una consulta.")
            else:
                ruta = exportar_resultado(RUTA_SALIDA, ultima_operacion, ultimo_resultado)
                print(f"[JSON] Resultado exportado a: {ruta}")

        elif opcion == "9":
            print("\nHasta luego. Gracias por usar SIRL.")
            break

        else:
            print("[!] Opcion no valida. Elige entre 1 y 9.")


def modo_api(puente: PuenteProlog):
    """
    Modo API: lee preferencias.json de Scala y exporta recomendaciones.json.
    Este modo es el que Scala invoca como subproceso.
    """
    try:
        preferencias = leer_preferencias(RUTA_ENTRADA)
    except FileNotFoundError as e:
        print(f"[ERROR] {e}")
        sys.exit(1)

    genero   = preferencias.get("genero_favorito", "programacion")
    autor    = preferencias.get("autor_favorito",  "ninguno")
    resultado = puente.obtener_recomendaciones(genero, autor)

    ruta_salida = os.path.join(BASE, "data", "salida", "recomendaciones.json")
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    with open(ruta_salida, "w", encoding="utf-8") as f:
        json.dump(resultado["recomendaciones"], f, ensure_ascii=False, indent=2)

    print(f"[API] {len(resultado['recomendaciones'])} recomendaciones exportadas.")


def main():
    parser = argparse.ArgumentParser(description="SIRL - Recomendador de Libros")
    parser.add_argument("--modo", choices=["menu", "api"], default="menu",
                        help="menu = interactivo, api = llamado desde Scala")
    args = parser.parse_args()

    print("[Python] Iniciando SIRL...")
    puente = PuenteProlog(RUTA_PROLOG)

    if args.modo == "api":
        modo_api(puente)
    else:
        modo_menu(puente)


if __name__ == "__main__":
    main()
