# Marco Teórico

## Sistemas de Recomendación

Un sistema de recomendación es una herramienta de software que sugiere ítems
relevantes a un usuario según sus preferencias previas o características conocidas.
En este proyecto se aplica un enfoque basado en contenido: se analiza el perfil
del usuario (géneros y autores preferidos) y se compara con los atributos de
los libros disponibles.

## Scala

Scala es un lenguaje de programación multiparadigma que combina programación
funcional y orientada a objetos. Corre sobre la JVM (Java Virtual Machine),
lo que le otorga alto rendimiento y compatibilidad. En SIRL, Scala actúa como
el coordinador central del sistema, manejando el flujo de datos entre módulos.

**Características clave usadas en SIRL:**
- Objetos y clases (`case class`) para modelar libros y usuarios.
- `App` trait para el punto de entrada del programa.
- Colecciones funcionales (`List`, `Map`, `filter`, `map`).

## Prolog

Prolog (Programming in Logic) es un lenguaje declarativo basado en lógica de
predicados de primer orden. Es especialmente adecuado para representar
conocimiento y realizar inferencias automáticas.

**Características clave usadas en SIRL:**
- **Hechos**: representan datos estáticos (libros, géneros, autores).
- **Reglas**: definen lógica de recomendación ("si el usuario prefiere X, recomendar Y").
- **Consultas**: permiten interrogar la base de conocimiento.

## Python

Python es un lenguaje interpretado de alto nivel, conocido por su simplicidad
y versatilidad. En SIRL, Python actúa como puente de integración entre Scala
y Prolog, usando la librería `pyswip` para comunicarse con SWI-Prolog.

**Características clave usadas en SIRL:**
- `pyswip`: librería que permite ejecutar consultas Prolog desde Python.
- Manejo de archivos JSON para leer preferencias del usuario.
- Scripts de integración que coordinan la comunicación entre módulos.

## Integración Multilenguaje

La integración entre los tres lenguajes sigue el siguiente flujo:

```
Usuario → Scala (entrada) → Python (puente) → Prolog (razonamiento) → Python (resultado) → Scala (salida)
```

Scala inicia el proceso, Python actúa de intermediario invocando consultas
Prolog, y los resultados regresan hasta Scala para ser presentados al usuario.
