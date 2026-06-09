# SIRL: Sistema Inteligente de Recomendación de Libros
> Arquitectura multilenguaje preparada para evolucionar a API REST.

## El problema que resuelve
Las librerías y bibliotecas dependen del conocimiento personal de sus libreros
para recomendar lecturas. SIRL automatiza ese proceso con lógica explícita
y transparente, con salida en JSON lista para conectar con web, app o API.

## Tecnologías y roles
| Lenguaje | Rol |
|----------|-----|
| **Scala**  | Coordinación, presentación, entrada del usuario |
| **Prolog** | Base de conocimiento, reglas de inferencia |
| **Python** | Puente de integración, menú interactivo, exportación JSON |

## Menú del sistema (9 funciones)
```
1. Buscar libro por titulo
2. Buscar libros por autor
3. Buscar libros por genero
4. Ver generos disponibles
5. Ver autores disponibles
6. Obtener recomendaciones
7. Estadisticas del sistema
8. Exportar resultado a JSON
9. Salir
```

## Cómo ejecutar

### Opción A — Solo Python + Prolog (más rápido, para demo)
```bash
cd python
pip install -r requirements.txt
python src/main.py
```

### Opción B — Sistema completo con Scala
```bash
cd scala
sbt run
```

### Opción C — Solo Prolog (prueba de conocimiento)
```bash
swipl -s prolog/consultas.pl
```

## Ejemplo de salida JSON (Opción 6 — Recomendaciones)
```json
{
  "genero_buscado": "ciencia_ficcion",
  "autor_buscado": "herbert",
  "total_recomendaciones": 5,
  "recomendaciones": [
    {
      "titulo": "Dune",
      "genero": "ciencia_ficcion",
      "autor": "herbert",
      "enlace_compra": "https://www.casadellibro.com/libro-dune"
    }
  ]
}
```
