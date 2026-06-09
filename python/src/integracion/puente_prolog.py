# =====================================================
# SIRL - Sistema Inteligente de Recomendación de Libros
# Archivo: integracion/puente_prolog.py
# Rol de Python: PUENTE entre Scala y Prolog.
#   Python no contiene lógica de recomendación.
#   Solo traduce pedidos de Scala en consultas Prolog
#   y devuelve resultados en formato JSON.
# =====================================================

from urllib.parse import quote
from pyswip import Prolog
import os

class PuenteProlog:
    """
    Puente entre Python y SWI-Prolog.
    Carga hechos.pl y reglas.pl, expone métodos
    que el menú principal invoca para cada opción.
    """

    def __init__(self, ruta_prolog: str):
        self.prolog = Prolog()
        ruta_hechos = os.path.abspath(os.path.join(ruta_prolog, "hechos.pl"))
        ruta_reglas = os.path.abspath(os.path.join(ruta_prolog, "reglas.pl"))
        self.prolog.consult(ruta_hechos)
        self.prolog.consult(ruta_reglas)
        print("[Prolog] Base de conocimiento cargada.")

    # -------------------------------------------------------
    # OPCIÓN 1: Buscar libro por título
    # -------------------------------------------------------
    def buscar_por_titulo(self, titulo: str) -> dict:
        resultados = list(self.prolog.query(
            f"buscar_libro('{titulo}', Genero, Autor)"
        ))
        if not resultados:
            return {"error": f"No se encontró el libro '{titulo}'"}
        r = resultados[0]
        return {
            "titulo":        titulo,
            "genero":        str(r["Genero"]),
            "autor":         str(r["Autor"]),
            "enlace_compra": self.generar_url_libro(titulo)
        }

    # -------------------------------------------------------
    # OPCIÓN 2: Buscar libros por autor
    # -------------------------------------------------------
    def buscar_por_autor(self, autor: str) -> dict:
        resultados = list(self.prolog.query(
            f"libros_por_autor({autor}, Titulo, Genero)"
        ))
        libros = [{
            "titulo": str(r["Titulo"]),
            "genero": str(r["Genero"]),
            "enlace_compra": self.generar_url_libro(str(r["Titulo"]))
        } for r in resultados]
        return {"autor": autor, "total": len(libros), "libros": libros}

    # -------------------------------------------------------
    # OPCIÓN 3: Buscar libros por género
    # -------------------------------------------------------
    def buscar_por_genero(self, genero: str) -> dict:

        resultados = list(
            self.prolog.query(
                f"libros_por_genero({genero}, Titulo, Autor)"
            )
        )

        libros = [
            {
                "titulo": str(r["Titulo"]),
                "autor": str(r["Autor"]),
                "enlace_compra": self.generar_url_libro(str(r["Titulo"]))
            }
            for r in resultados
        ]

        return {
            "genero": genero,
            "total": len(libros),
            "libros": libros
        }

    # -------------------------------------------------------
    # OPCIÓN 4: Ver géneros disponibles
    # -------------------------------------------------------
    def generos_disponibles(self) -> dict:
        resultados = list(self.prolog.query("genero_disponible(Genero)"))
        generos = sorted(set(str(r["Genero"]) for r in resultados))
        return {"generos_disponibles": generos, "total": len(generos)}

    # -------------------------------------------------------
    # OPCIÓN 5: Ver autores disponibles
    # -------------------------------------------------------
    def autores_disponibles(self) -> dict:
        resultados = list(self.prolog.query("autor_disponible(Autor)"))
        autores = sorted(set(str(r["Autor"]) for r in resultados))
        return {"autores_disponibles": autores, "total": len(autores)}

    # -------------------------------------------------------
    # OPCIÓN 6: Obtener recomendaciones (lógica principal)
    # -------------------------------------------------------
    def obtener_recomendaciones(self, genero: str, autor: str) -> dict:

        consulta = f"recomendar({genero}, {autor}, Titulo)"
        resultados = list(self.prolog.query(consulta))

        vistos = set()
        recomendados = []

        for r in resultados:

            titulo = str(r["Titulo"])

            if titulo in vistos:
                continue

            vistos.add(titulo)

            info = list(
                self.prolog.query(
                    f"libro(_, '{titulo}', Genero, Autor)"
                )
            )

            if info:

                url_real = self.generar_url_libro(titulo)

                recomendados.append({
                    "titulo": titulo,
                    "genero": str(info[0]["Genero"]),
                    "autor": str(info[0]["Autor"]),
                    "enlace_compra": url_real
                })

        return {
            "genero_buscado": genero,
            "autor_buscado":  autor,
            "total_recomendaciones": len(recomendados),
            "recomendaciones": recomendados
        }

    # -------------------------------------------------------
    # OPCIÓN 7: Estadísticas del sistema
    # -------------------------------------------------------
    def obtener_estadisticas(self) -> dict:
        todos_libros = list(self.prolog.query("libro(_, _, _, _)"))
        total_libros  = len(todos_libros)

        autores  = set(str(r["Autor"]) for r in
                       self.prolog.query("libro(_, _, _, Autor)"))
        generos_raw = list(self.prolog.query("genero_disponible(Genero)"))
        generos_unicos = set(str(r["Genero"]) for r in generos_raw)

        conteo_generos = {}
        for g in generos_unicos:
            total = list(self.prolog.query(f"total_por_genero({g}, Total)"))
            conteo_generos[g] = int(total[0]["Total"]) if total else 0

        return {
            "total_libros":   total_libros,
            "total_autores":  len(autores),
            "total_generos":  len(generos_unicos),
            "libros_por_genero": conteo_generos
        }

    # -------------------------------------------------------
    # Generar url libro
    # -------------------------------------------------------
    def generar_url_libro(self, titulo):
        return f"https://openlibrary.org/search?q={quote(titulo)}"
