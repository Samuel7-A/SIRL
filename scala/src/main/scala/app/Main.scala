// =====================================================
// SIRL - Sistema Inteligente de Recomendación de Libros
// Archivo: Main.scala
// Descripción: Punto de entrada principal del sistema
// =====================================================

package app

import app.modelos.Usuario
import app.servicios.RecomendadorService
import scala.io.StdIn.readLine

object Main extends App {

  println("=" * 50)
  println("  SIRL: Sistema Inteligente de Recomendación de Libros")
  println("=" * 50)
  println()

  // -------------------------------------------------------
  // PASO 1: Capturar preferencias del usuario
  // -------------------------------------------------------
  println("Bienvenido. Por favor ingresa tus preferencias:")
  print("Tu nombre: ")
  val nombre = readLine()

  println("\nGéneros disponibles: programacion, algoritmos, inteligencia_artificial,")
  println("  ciencia_ficcion, distopia, terror, fantasia, historia, ciencia, clasico")
  print("Tu género favorito: ")
  val genero = readLine()

  println("\nAutores disponibles: martin, hunt, gamma, cormen, russell, herbert,")
  println("  orwell, huxley, king, tolkien, rowling, harari, hawking, fitzgerald")
  print("Tu autor favorito (o presiona Enter para omitir): ")
  val autorInput = readLine()
  val autor = if (autorInput.trim.isEmpty) "ninguno" else autorInput.trim

  // Crear el objeto usuario con sus preferencias
  val usuario = Usuario(
    nombre         = nombre,
    generoFavorito = genero,
    autorFavorito  = autor
  )

  println(s"\n$usuario")
  println()

  // -------------------------------------------------------
  // PASO 2: Guardar preferencias en JSON para Python/Prolog
  // -------------------------------------------------------
  RecomendadorService.escribirPreferencias(usuario)

  // -------------------------------------------------------
  // PASO 3: Invocar Python que consultará Prolog
  // -------------------------------------------------------
  val exito = RecomendadorService.ejecutarModuloPython()

  // -------------------------------------------------------
  // PASO 4: Leer y mostrar las recomendaciones
  // -------------------------------------------------------
  if (exito) {
    val recomendaciones = RecomendadorService.leerRecomendaciones()

    println()
    println("=" * 50)
    println(s"  Recomendaciones para ${usuario.nombre}:")
    println("=" * 50)

    if (recomendaciones.isEmpty) {
      println("No se encontraron recomendaciones para tus preferencias.")
    } else {
      recomendaciones.zipWithIndex.foreach { case (libro, i) =>
        println(s"${i + 1}. $libro")
      }
    }
  } else {
    println("\n[Error] No se pudo completar la recomendación. Verifica que Python esté instalado.")
  }

  println()
  println("Gracias por usar SIRL.")
}
