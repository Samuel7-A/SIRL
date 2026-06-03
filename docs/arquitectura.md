# Arquitectura del Sistema

## Visión General

SIRL adopta una arquitectura modular de tres capas, donde cada lenguaje
tiene una responsabilidad clara y bien definida.

```
┌─────────────────────────────────────────────┐
│              MÓDULO SCALA                   │
│   Lógica principal · Entrada del usuario    │
│   Coordinación · Presentación de resultados │
└─────────────────┬───────────────────────────┘
                  │ llama vía proceso externo
                  ▼
┌─────────────────────────────────────────────┐
│              MÓDULO PYTHON                  │
│   Puente de integración · Lee JSON          │
│   Invoca consultas Prolog · Devuelve JSON   │
└─────────────────┬───────────────────────────┘
                  │ consultas via pyswip
                  ▼
┌─────────────────────────────────────────────┐
│              MÓDULO PROLOG                  │
│   Base de conocimiento · Hechos             │
│   Reglas de inferencia · Consultas          │
└─────────────────────────────────────────────┘
```

## Flujo de Datos

1. El usuario ejecuta el sistema desde **Scala**.
2. Scala escribe las preferencias del usuario en `data/entrada/preferencias.json`.
3. Scala invoca el script **Python** como subproceso.
4. Python lee el JSON, formula la consulta y la lanza sobre **Prolog**.
5. Prolog aplica sus reglas y devuelve los libros recomendados.
6. Python escribe los resultados en `data/salida/recomendaciones.json`.
7. Scala lee el JSON de salida y presenta los resultados al usuario.

## Módulos del Sistema

### Módulo Scala
- `Main.scala`: punto de entrada, coordina el flujo completo.
- `modelos/Libro.scala`: modelo de datos para libros.
- `modelos/Usuario.scala`: modelo de datos para usuarios.
- `servicios/RecomendadorService.scala`: lógica de coordinación.

### Módulo Prolog
- `hechos.pl`: base de datos de libros (título, género, autor).
- `reglas.pl`: reglas de recomendación basadas en preferencias.
- `consultas.pl`: consultas predefinidas para usar desde Python.

### Módulo Python
- `main.py`: script principal que orquesta la integración.
- `integracion/puente_prolog.py`: interfaz con SWI-Prolog via pyswip.
- `utils/lector_datos.py`: utilidades para leer y escribir JSON.
