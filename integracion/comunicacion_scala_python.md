# Comunicación: Scala → Python

## ¿Cómo se comunican Scala y Python?

Scala invoca Python como un **subproceso externo** usando `scala.sys.process._`.
La comunicación se realiza mediante archivos JSON en la carpeta `data/`.

## Flujo de comunicación

```
Scala                          Python
  │                              │
  │── escribe preferencias.json ─►│
  │                              │
  │── ejecuta: python main.py ──►│
  │                              │── consulta Prolog
  │                              │── recibe resultados
  │                              │── escribe recomendaciones.json
  │                              │
  │◄── lee recomendaciones.json ─│
  │                              │
  │── muestra resultados ────────│
```

## Archivo de entrada: `data/entrada/preferencias.json`

Generado por Scala con las preferencias del usuario:

```json
{
  "nombre": "Ana",
  "genero_favorito": "terror",
  "autor_favorito": "king"
}
```

## Archivo de salida: `data/salida/recomendaciones.json`

Generado por Python con los libros recomendados:

```json
[
  { "titulo": "It", "genero": "terror", "autor": "king" },
  { "titulo": "The Shining", "genero": "terror", "autor": "king" }
]
```

## Código Scala relevante

```scala
// Ejecutar Python como subproceso
val resultado = "python ../python/src/main.py".!
```

## Requisitos

- Python 3.8 o superior instalado y en el PATH del sistema.
- Librería `pyswip` instalada: `pip install -r python/requirements.txt`
