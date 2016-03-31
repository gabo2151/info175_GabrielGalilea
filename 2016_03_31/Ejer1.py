class Auto_CLASS:
	def __init__(self, kmt, oil, rnd, stat):
		self.kmt = kmt #Kilometraje
		self.oil = oil #Bencina
		self.rnd = rnd #Rendimiento
		self.stat = stat #Encendido (True or False)

	def Encender(self):
		if self.stat == False:
			self.stat = True

	def Apagar(self):
		if self.stat:
			self.stat = False

	def Mover(self, km):
		if km <= (self.rnd*self.oil):
			self.kmt += km
			self.oil -= km/self.rnd
		else:
			print "No hay suficiente combustible"

	def getKilometraje(self):
		return self.kmt

	def getBencina(self):
		return self.oil

	def loadBencina(self, oil):
		if self.stat:
			print "Apaga el vehiculo antes de cargar bencina"
		else:
			self.oil += oil

if __name__ == "__main__":
	camioneta = Auto_CLASS(0, 0, 9, False)
	print "Combustible: %s" % camioneta.getBencina()
	camioneta.loadBencina( int(raw_input("Litros de Bencina a cargar: ")) )
	print "Combustible: %s" % camioneta.getBencina()

	camioneta.Encender()
	camioneta.Mover( int(raw_input("Kilometros que se desea desplazar: ")) )
	print "Kilometraje: %s" % camioneta.getKilometraje()