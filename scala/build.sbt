// =====================================================
// SIRL - Sistema Inteligente de Recomendación de Libros
// Archivo: build.sbt
// =====================================================

name := "SIRL"
version := "1.0.0"
scalaVersion := "2.13.12"

// Librería para parsear JSON en Scala
libraryDependencies += "com.typesafe.play" %% "play-json" % "2.10.0-RC5"

// Configuración del punto de entrada
Compile / mainClass := Some("app.Main")
