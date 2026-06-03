# SIRL: Sistema Inteligente de Recomendación de Libros

Sistema multilenguaje que integra **Scala**, **Prolog** y **Python** para recomendar libros según las preferencias del usuario.

## Tecnologías

| Lenguaje | Rol |
|----------|-----|
| Scala    | Lógica principal y coordinación del sistema |
| Prolog   | Base de conocimiento y reglas de recomendación |
| Python   | Integración entre módulos y procesamiento de datos |

## Estructura del Proyecto

```
SIRL-sistema-recomendacion-libros/
├── docs/               → Documentación del proyecto
├── scala/              → Módulo principal en Scala
├── prolog/             → Base de conocimiento en Prolog
├── python/             → Módulo de integración en Python
├── integracion/        → Documentación de comunicación entre lenguajes
├── data/               → Datos de entrada y salida
├── README.md
└── LICENSE
```

## Cómo ejecutar

### Prolog
```bash
swipl -s prolog/hechos.pl prolog/reglas.pl prolog/consultas.pl
```

### Python
```bash
cd python
pip install -r requirements.txt
python src/main.py
```

### Scala
```bash
cd scala
sbt run
```

## Autores
Proyecto académico — Programación Multilenguaje
