class Docente:
	def __init__(self, nom, ape, tit):
		self.nombre = nom
		self.apellido = ape
		self.titulo = tit
	
	def agregarnombre(self, nom):
		self.nombre = nom
	def obtenernombre(self):
		return self.nombre
	def agregarapellido(self, ape):
		self.apellido = ape
	def obtenerapellido(self):
		return self.apellido
	def agregartitulo(self, tit):
		self.titulo = tit
	def obtenertitulo(self):
		return self.titulo
		
	def presentar(self):
		cadena = "Nombre: %s Apellido: %s Titulo:%s"%(self.obtenernombre(),self.obtenerapellido(),self.obtenertitulo())
		return cadena