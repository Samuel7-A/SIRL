// =====================================================
// SIRL - Sistema Inteligente de Recomendación de Libros
// Archivo: servicios/RecomendadorService.scala
// Descripción: Servicio que coordina la recomendación de libros
//              invocando el script Python como subproceso
// =====================================================

package app.servicios

import app.modelos.{Libro, Usuario}
import scala.sys.process._
import scala.io.Source
import java.io.{File, PrintWriter}

object RecomendadorService {

  // Rutas de los archivos de comunicación entre módulos
  private val rutaEntrada   = "../data/entrada/preferencias.json"
  private val rutaSalida    = "../data/salida/recomendaciones.json"
  private val rutaScriptPy  = "../python/src/main.py"

  // -------------------------------------------------------
  // Paso 1: Escribir las preferencias del usuario en JSON
  // -------------------------------------------------------
  def escribirPreferencias(usuario: Usuario): Unit = {
    val json =
      s"""{
         |  "nombre": "${usuario.nombre}",
         |  "genero_favorito": "${usuario.generoFavorito}",
         |  "autor_favorito": "${usuario.autorFavorito}"
         |}""".stripMargin

    val writer = new PrintWriter(new File(rutaEntrada))
    try {
      writer.write(json)
      println(s"[Scala] Preferencias guardadas en: $rutaEntrada")
    } finally {
      writer.close()
    }
  }

  // -------------------------------------------------------
  // Paso 2: Invocar el script Python como subproceso
  // -------------------------------------------------------
  def ejecutarModuloPython(): Boolean = {
    println("[Scala] Invocando módulo Python para consultar Prolog...")
    val resultado = s"python $rutaScriptPy".!
    if (resultado == 0) {
      println("[Scala] Módulo Python ejecutado correctamente.")
      true
    } else {
      println(s"[Scala] Error al ejecutar Python. Código de salida: $resultado")
      false
    }
  }

  // -------------------------------------------------------
  // Paso 3: Leer las recomendaciones generadas por Python
  // -------------------------------------------------------
  def leerRecomendaciones(): List[Libro] = {
    val archivo = new File(rutaSalida)
    if (!archivo.exists()) {
      println("[Scala] No se encontró el archivo de recomendaciones.")
      return List.empty
    }

    val contenido = Source.fromFile(rutaSalida).mkString
    // Parseo simple del JSON de recomendaciones (sin librerías externas)
    // Formato esperado: [{"titulo":"X","genero":"Y","autor":"Z"}, ...]
    val patron = """"titulo":"([^"]+)","genero":"([^"]+)","autor":"([^"]+)"""".r
    patron.findAllMatchIn(contenido).map { m =>
      Libro(titulo = m.group(1), genero = m.group(2), autor = m.group(3))
    }.toList
  }
}
