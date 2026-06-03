# =====================================================
# SIRL - Sistema Inteligente de Recomendación de Libros
# Archivo: integracion/puente_prolog.py
# Descripción: Módulo que conecta Python con SWI-Prolog
#              usando la librería pyswip
# =====================================================

from pyswip import Prolog
import os

class PuenteProlog:
    """
    Clase que actúa como puente entre Python y Prolog.
    Carga los archivos .pl y ejecuta consultas de recomendación.
    """

    def __init__(self, ruta_base: str):
        """
        Inicializa el motor Prolog y carga los archivos de conocimiento.
        ruta_base: ruta relativa a la carpeta 'prolog/' del proyecto
        """
        self.prolog = Prolog()
        
        # Cargar hechos y reglas (el orden importa: primero hechos, luego reglas)
        ruta_hechos = os.path.join(ruta_base, "hechos.pl")
        ruta_reglas = os.path.join(ruta_base, "reglas.pl")
        
        # Convertir a ruta absoluta para evitar problemas de directorio
        ruta_hechos = os.path.abspath(ruta_hechos)
        ruta_reglas = os.path.abspath(ruta_reglas)
        
        self.prolog.consult(ruta_hechos)
        self.prolog.consult(ruta_reglas)
        print(f"[Python-Prolog] Base de conocimiento cargada correctamente.")

    def obtener_recomendaciones(self, genero: str, autor: str) -> list:
        """
        Consulta Prolog con el género y autor favorito del usuario.
        Retorna una lista de diccionarios con los libros recomendados.
        """
        # Construir la consulta Prolog
        consulta = f"recomendar({genero}, {autor}, Titulo)"
        print(f"[Python-Prolog] Ejecutando consulta: {consulta}")
        
        resultados = []
        titulos_vistos = set()  # Para evitar duplicados

        for solucion in self.prolog.query(consulta):
            titulo = str(solucion["Titulo"])
            
            # Evitar libros duplicados en los resultados
            if titulo not in titulos_vistos:
                titulos_vistos.add(titulo)
                
                # Obtener también el género y autor del libro recomendado
                info = list(self.prolog.query(
                    f"libro(_, '{titulo}', Genero, Autor)"
                ))
                
                if info:
                    resultados.append({
                        "titulo": titulo,
                        "genero": str(info[0]["Genero"]),
                        "autor":  str(info[0]["Autor"])
                    })

        print(f"[Python-Prolog] Se encontraron {len(resultados)} recomendaciones.")
        return resultados
