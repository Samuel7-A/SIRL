// =====================================================
// SIRL - Sistema Inteligente de Recomendación de Libros
// Archivo: modelos/Usuario.scala
// Descripción: Modelo de datos para representar un usuario
// =====================================================

package app.modelos

// case class que representa las preferencias del usuario
case class Usuario(
  nombre: String,
  generoFavorito: String,
  autorFavorito: String = "ninguno"   // valor por defecto si no tiene autor favorito
) {
  override def toString: String =
    s"👤 Usuario: $nombre | Género favorito: $generoFavorito | Autor favorito: $autorFavorito"
}
