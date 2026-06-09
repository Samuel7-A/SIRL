package app.modelos

case class Usuario(
  nombre:         String,
  generoFavorito: String,
  autorFavorito:  String = "ninguno"
) {
  override def toString: String =
    s"Usuario: $nombre | Género: $generoFavorito | Autor: $autorFavorito"
}
