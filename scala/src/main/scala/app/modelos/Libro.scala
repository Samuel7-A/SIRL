// =====================================================
// SIRL - Sistema Inteligente de Recomendación de Libros
// Archivo: modelos/Libro.scala
// Descripción: Modelo de datos para representar un libro
// =====================================================

package app.modelos

// case class: forma funcional de definir un modelo de datos en Scala
// Genera automáticamente: equals, hashCode, toString, copy
case class Libro(
  titulo: String,
  genero: String,
  autor: String
) {
  override def toString: String =
    s"📖 '$titulo' | Género: $genero | Autor: $autor"
}
