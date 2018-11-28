from personal_academico.Docente import *
class Alumno:
	def __init__(self, nom, mate, soci):
		self.nombre = nom
		self.docente_matematica = Docente()
		self.docente_sociales = Docente()

	def agregarnombre(self, nom):
		self.nombres = nom
	def obtenernombre(self):
		return self.nombre
	def agregardocente_matematica(self, mate):
		self.docentematematica = mate
	def obtenerdocente_matematica(self):
		return self.docente_matematica
	def agregardocente_sociales(self, soci):
		self.docente_sociales = soci
	def obtenerdocente_sociales(self):
		return self.docente_sociales

	def presentar(self):
		cadena = "Nombres: %s Apellidos: %s Titulos:%s\n"%(self.obtenernombre(),self.Docente.obtenerdocente_matematica(),self.Docente.obtenerdocente_sociales())
		return cadena