class Equipo():
	def __init__(self,equi,pa):
		self.nombre=equi
		self.pais=pa
	def agregarnombre(self,equi):
		self.nombre = equi
	def obtenernombre(self):
		return self.nombre
	def agregarpais(self,pa):
		self.pais = pa
	def obtenerpais(self):
		return self.pais


class Futbolista():

	def __init__(self,nom="",ape="",equi="",pos="",dorsal=0):
		self.nombre = nom
		self.apellido=ape
		self.equipo=equi
		self.posicion=pos
		self.dorsal=dorsal

	def agregarnombre(self,nom):
		self.nombre = nom
	def obtenernombre(self):
		return self.nombre
	def agregarapellido(self,ape):
		self.apellido = ape
	def obtenerapellido(self):
		return self.apellido
	def agregardorsal(self,dor):
		self.dorsal = dor
	def obtenerdorsal(self):
		return self.dorsal
	def agregarposicion(self,pos):
		self.posicion = pos
	def obtenerposicion(self):
		return self.posicion
	def agregarequipo(self, equi):
		self.equipo = equi
	def obtenerequipo(self):
		return self.equipo
	
	def presentar(self):
		cadena="%s %s pertenece al equipo:%s del pais: %s, su posicion es:%s y su dorsal es el numero:%d" %(self.obtenernombre(),self.obtenerapellido(),self.obtenerequipo().obtenernombre(),self.obtenerequipo().obtenerpais(),self.obtenerposicion(),self.obtenerdorsal())
		return cadena