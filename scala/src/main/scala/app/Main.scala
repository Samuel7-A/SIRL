// =====================================================
// SIRL - Sistema Inteligente de Recomendación de Libros
// Archivo: Main.scala
// Rol de Scala: COORDINADOR y PRESENTACIÓN.
//   Scala captura las preferencias del usuario,
//   invoca Python (que consulta Prolog), lee el JSON
//   de respuesta y presenta los resultados formateados.
//   Arquitectura preparada para evolucionar a API REST.
// =====================================================

package app

import app.modelos.Usuario
import app.servicios.RecomendadorService
import scala.io.StdIn.readLine
import scala.sys.process._

object Main extends App {

  println("=" * 55)
  println("  SIRL: Sistema Inteligente de Recomendación de Libros")
  println("  Arquitectura: Scala → Python → Prolog → JSON")
  println("=" * 55)

  println("\n1. Recomendación rápida")
  println("2. Menú completo (Python)")
  println("3. Salir")

  print("\nSelecciona una opción: ")
  val opcion = readLine()

  opcion match {

    case "1" =>

      print("\nTu nombre: ")
      val nombre = readLine()

      println("\nGéneros: programacion, algoritmos, inteligencia_artificial,")
      println("  ciencia_ficcion, distopia, terror, fantasia, historia, ciencia, clasico")

      print("Tu género favorito: ")
      val genero = readLine()

      print("Tu autor favorito (Enter para omitir): ")
      val autorInput = readLine()

      val autor =
        if (autorInput.trim.isEmpty) "ninguno"
        else autorInput.trim

      val usuario = Usuario(nombre, genero, autor)

      RecomendadorService.escribirPreferencias(usuario)

      val exito = RecomendadorService.ejecutarModuloPython()

      if (exito) {

        val recomendaciones =
          RecomendadorService.leerRecomendaciones()

        println()
        println("=" * 55)
        println(s"Recomendaciones para ${usuario.nombre}")
        println("=" * 55)

        recomendaciones.zipWithIndex.foreach {
          case (libro, i) =>
            println(s"\n${i + 1}. ${libro.titulo}")
            println(s"   Género : ${libro.genero}")
            println(s"   Autor  : ${libro.autor}")
            println(s"   URL    : ${libro.enlaceCompra}")
        }

      } else {
        println("[ERROR] No se pudo ejecutar Python.")
      }

  case "2" =>

    println("\nAbriendo menú completo de Python...\n")

    Process(
      Seq(
        "cmd",
        "/c",
        "start",
        "cmd",
        "/k",
        "python ../python/src/main.py"
      )
    ).!

    case "3" =>
      println("Hasta luego.")

    case _ =>
      println("Opción inválida.")
  }
}
