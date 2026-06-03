# Comunicación: Python → Prolog

## ¿Cómo se comunican Python y Prolog?

Python se comunica con Prolog usando la librería **pyswip**, que es un
wrapper de Python para SWI-Prolog. Permite cargar archivos `.pl` y
ejecutar consultas directamente desde Python.

## Instalación

```bash
# 1. Instalar SWI-Prolog en el sistema
#    Windows: https://www.swi-prolog.org/download/stable
#    Linux:   sudo apt-get install swi-prolog
#    macOS:   brew install swi-prolog

# 2. Instalar pyswip
pip install pyswip==0.2.10
```

## Cómo funciona pyswip

```python
from pyswip import Prolog

# Crear instancia del motor Prolog
prolog = Prolog()

# Cargar archivos .pl
prolog.consult("prolog/hechos.pl")
prolog.consult("prolog/reglas.pl")

# Ejecutar una consulta
for solucion in prolog.query("recomendar(terror, king, Titulo)"):
    print(solucion["Titulo"])
    # Output: It
    # Output: The Shining
```

## Consulta principal de SIRL

La consulta que Python lanza a Prolog es:

```prolog
recomendar(GeneroFavorito, AutorFavorito, Titulo)
```

Donde:
- `GeneroFavorito`: género que el usuario prefiere (ej: `terror`)
- `AutorFavorito`: autor favorito del usuario (ej: `king`) o `ninguno`
- `Titulo`: variable que Prolog instancia con cada libro recomendado

## Requisitos

- SWI-Prolog instalado en el sistema operativo.
- La variable `SWI_HOME_DIR` debe estar configurada si pyswip no encuentra SWI-Prolog automáticamente.
