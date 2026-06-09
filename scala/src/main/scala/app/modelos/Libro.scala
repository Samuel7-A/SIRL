package app.modelos

case class Libro(
  titulo:       String,
  genero:       String,
  autor:        String,
  enlaceCompra: String = ""
)
