package app.servicios

import app.modelos.{Libro, Usuario}
import scala.sys.process._
import scala.io.Source
import java.io.{File, PrintWriter}

object RecomendadorService {

  private val rutaEntrada  = "../data/entrada/preferencias.json"
  private val rutaSalida   = "../data/salida/recomendaciones.json"
  private val rutaScriptPy = "../python/src/main.py"

  def escribirPreferencias(usuario: Usuario): Unit = {
    val json =
      s"""{"nombre":"${usuario.nombre}","genero_favorito":"${usuario.generoFavorito}","autor_favorito":"${usuario.autorFavorito}"}"""
    val w = new PrintWriter(new File(rutaEntrada))
    try { w.write(json); println("[Scala] Preferencias guardadas.") }
    finally { w.close() }
  }

  def ejecutarModuloPython(): Boolean = {
    println("[Scala] Invocando Python → Prolog...")
    s"python $rutaScriptPy --modo api".! == 0
  }

  def leerRecomendaciones(): List[Libro] = {
    val archivo = new File(rutaSalida)

    if (!archivo.exists()) return List.empty

    val contenido = Source.fromFile(archivo)("UTF-8").mkString

    val patron =
      """"titulo"\s*:\s*"([^"]+)"[\s\S]*?"genero"\s*:\s*"([^"]+)"[\s\S]*?"autor"\s*:\s*"([^"]+)"[\s\S]*?"enlace_compra"\s*:\s*"([^"]+)"""".r

    patron.findAllMatchIn(contenido).map { m =>
      Libro(
        m.group(1),
        m.group(2),
        m.group(3),
        m.group(4)
      )
    }.toList
  }

}
