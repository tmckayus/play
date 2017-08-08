scalaHome := Some(file("/opt/scala"))
scalaVersion := "2.11.8"

name := "SparkPi"

version := "0.1"
unmanagedSourceDirectories in Compile := (scalaSource in Compile).value :: Nil

libraryDependencies += "org.apache.spark" % "spark-sql_2.11" % "2.1.0" % "provided"
