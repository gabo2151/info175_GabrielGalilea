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

class Camion_CLASS(Auto_CLASS):
	def __init__(self, kmt, oil, rnd, stat, ps, rued, acop):
		self.kmt = kmt #Kilometraje
		self.oil = oil #Bencina
		self.rnd = rnd #Rendimiento
		self.stat = stat #Encendido (True or False)
		self.peso = ps #Peso [float]
		self.rued = rued #Ruedas [int]
		self.acop = acop #Acoplado [lista]

	def setAcoplado(self, pes, rue, aco):
		self.acop.append( [pes, rue, aco] )

	def delAcoplado(self):
		for i in range(self.acop):
			self.acop.pop()

	def getAcoplado(self):
		return self.acop

	def getRuedas(self):
		return self.rued

	def getPeso(self):
		return self.peso

if __name__ == "__main__":
	camioneta = Camion_CLASS(0, 0, 9, False, 2.45, 12, [])
	print "Combustible: %s" % camioneta.getBencina()
	camioneta.loadBencina( float(raw_input("Litros de Bencina a cargar: ")) )
	print "Combustible: %s" % camioneta.getBencina()

	camioneta.Encender()
	camioneta.Mover( float(raw_input("Kilometros que se desea desplazar: ")) )
	print "Kilometraje: %s" % camioneta.getKilometraje()
	print "Combustible: %s" % camioneta.getBencina()
