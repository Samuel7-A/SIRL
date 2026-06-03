# Conclusiones

## Resultados Obtenidos

El desarrollo de SIRL demostró que es posible construir un sistema funcional
e inteligente combinando tres paradigmas de programación distintos. Cada lenguaje
aportó sus fortalezas naturales al sistema:

- **Prolog** resultó ideal para representar el conocimiento sobre libros y
  definir reglas de recomendación de forma declarativa y legible.
- **Scala** demostró su capacidad para coordinar sistemas complejos con una
  sintaxis expresiva y tipado estático que previene errores.
- **Python** facilitó enormemente la integración entre módulos gracias a su
  ecosistema de librerías y su simplicidad para manejar archivos y procesos.

## Lecciones Aprendidas

1. La separación clara de responsabilidades entre módulos facilita el
   desarrollo, la prueba y el mantenimiento del sistema.
2. La comunicación entre lenguajes mediante archivos JSON es una estrategia
   simple y efectiva para sistemas académicos y de prototipado.
3. La arquitectura multilenguaje, aunque añade complejidad inicial, permite
   resolver cada subproblema con la herramienta más adecuada.

## Trabajo Futuro

- Ampliar la base de conocimiento Prolog con más libros y géneros.
- Implementar recomendación colaborativa (basada en otros usuarios).
- Agregar una interfaz de línea de comandos más amigable en Scala.
- Explorar integración con APIs externas de catálogos de libros.

## Reflexión Final

Este proyecto evidencia que el paradigma multilenguaje no es una limitación,
sino una ventaja competitiva cuando se aplica con una arquitectura bien
pensada y responsabilidades claramente definidas entre módulos.
