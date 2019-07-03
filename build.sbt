import sbt.Keys._
import sbt.Process
import sbtassembly.AssemblyPlugin.autoImport.ShadeRule

val mammutKtTv          = "0.3.109"

lazy val commonSettings = Seq(
    organization := "com.mammut",
    version      := mammutKtTv,
    scalaVersion := scalaV
)


assemblyShadeRules in assembly := Seq(
    ShadeRule.rename("com.google.protobuf.*" -> "shadedproto.@1").inProject.inLibrary(protoBuf).inProject
)

val ignoreConflictingTestsEnv = System.getenv("IGNORE_CONFLICTING_TESTS")
val ignoreConflictingTests: Boolean = (ignoreConflictingTestsEnv != null && ignoreConflictingTestsEnv.toLowerCase.contains("true"))

//testOptions in Test += Tests.Argument("-l", "ConflictingTest")

concurrentRestrictions in Global += Tags.limit(Tags.Test, 1)
