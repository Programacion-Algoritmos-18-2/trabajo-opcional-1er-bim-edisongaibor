class Garante(object):
	def __init__(self):
		self.nombre = ""
		self.apellido = ""
		self.sueldo= 0
	
	def agregarnombre(self, nom):
		self.nombre = nom
	def obtenernombre(self):
		return self.nombre
	def agregarapellido(self, ape):
		self.apellido = ape
	def obtenerapellido(self):
		return self.apellido
	def agregarsueldo(self, suel):
		self.sueldo = suel
	def obtenersueldo(self):
		return self.sueldo
	def __str__(self):
		return "Nombre:%s Apellido:%s Sueldo:%f"%(self.obtenernombre(), self.obtenerapellido(), self.obtenersueldo())	

class Prestamo(object):
	def __init__(self):
		self.nombrebeneficiario = ""
		self.montoprestamo = 0
		self.interes = 0
		self.tiempoprestamo = 0
		self.garante= Garante()

	def agregarnombrebeneficiario(self, nom):
		self.nombre = nom
	def obtenernombrebeneficiario(self):
		return self.nombre
	def agregarmontoprestamo(self, mont):
		self.montoprestamo = mont
	def obtenermontoprestamo(self):
		return self.montoprestamo	
	def agregarinteres(self, inter):
		self.interes = inter
	def obtenerinteres(self):
		return self.interes
	def agregartiempoprestamo(self, tp):
		self.tiempoprestamo = tp
	def obtenertiempoprestamo(self):
		return self.tiempoprestamo
	def agregargarante(self, ga):
		self.garante = ga
	def obtenergarante(self):
		return self.garante
	
	def __str__(self):
		return "Nombre del Beneficiario:%s Monto del Prestamo:%.2f Interes:%.2f%% Tiempo de prestamos en años:%d\nGarante:%s\n" %(self.obtenerNombreBene(), self.obtenerMontoP(), self.obtenerInteres(), self.obtenerTiempoPrestamo(), self.obtenerGarante1())

class PrestamosAutomovil(Prestamo):
	def __init__(self):
		super(PrestamosAutomovil, self).__init__()
		self.tipoVehiculo= ""
		self.marcaVehiculo= ""
		self.garante2 = Garante()
	
	def agregartipovehiculo(self, tipo):
		self.tipovehiculo = tipo
	def obtenertipovehiculo(self):
		return self.tipovehiculo
	def agregarmarcavehiculo(self, marca):
		self.marcavehiculo = marca
	def obtenermarcavehiculo(self):
		return self.marcavehiculo
	def establecergarante2(self, ga2):
		self.garante2 = ga2
	def obtenergarante2(self):
		return self.garante2
	def __str__(self):
		return "%sTipo de vehiculo:%s\tMarca de vehiculo:%s\n Garante:%s\n"%(super(Prestamos, self).__str__(),self.obtenertipoVehiculo(),self.obtenermarcaVehiculo(),self.obtenergarante2())			 			


		