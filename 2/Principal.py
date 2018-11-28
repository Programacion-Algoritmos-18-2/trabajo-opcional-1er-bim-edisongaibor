from personal_academico.Docente import *
from sector_estudiantil.Alumno import *
NombreDocente1 = input("Ingrese nombre del Docente:\n")
ApellidoDocente1 = input("Ingrese apellido del Docente:\n")
TituloDocente11 = input("Ingrese titulo del docente:\n")

Docente1 = Docente(NombreDocente1, ApellidoDocente1, TituloDocente1)
Docente2 = Docente(NombreDocente1, ApellidoDoce1, TituloDocente1)

NombreAlumno = input("Ingrese nombre alumno:\n")
alum = Alumno(NombreAlumno, Docente1, Docente2)
alum.presentar()