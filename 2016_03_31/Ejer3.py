class Persona(object):
	def __init__(self, run, nom, bd, gen):
		self.run = run #Rol Unico Nominativo
		self.nom = nom #Nombre
		self.bd = bd #Fecha de Nacimiento
		self.gen = gen #Genero

	def getEdad(self):
		return self.bd

class nota:
	def __init__(self, val, pond, ramo, carr):
		self.val = val #Valor nota
		self.pond = pond #Ponderacion
		self.ramo = ramo #Ramo
		self.carr = carr #Carrera

	def getNota(self):
		return self.val

	def getPonderacion(self):
		return self.pond

	def modValor(self, value, opc):
		if opc == 0: #Modifica la nota
			self.val = float(value)
		elif opc == 1: #Modifica la ponderacion
			self.pond = float(value)
		elif opc == 2: #Modifica el ramo
			self.ramo = value
		elif opc == 3: #Modifica la carrera
			self.carr = value

class Alumno(Persona):
	def __init__(self, run, nom, bd, gen, mail, carr, prom):
		Persona.__init__(self, run, nom, bd, gen)
		self.mail = mail
		self.carr = carr #Carrera
		self.prom = prom #Promocion (Anio de ingreso)
		self.notas = [] #En lista

	def addNota(self, lNota): # SE DEBE INGRESAR COMO UNA LISTA
		nuevaNota = nota(lNota[0], lNota[1], lNota[2], lNota[3])
		self.notas.append[nuevaNota]
		print "Nota registrada"

	def getPPR(self):
		dN = {}
		for i in range( len(self.notas) ):
			if dN.has_key( self.notas[i].ramo ):
				dN[ self.notas[i].ramo ] += self.notas[i].val*self.notas[i].pond
			else:
				dN[ self.notas[i].ramo ] = self.notas[i].val*self.notas[i].pond
		return dN

	def getPGA(self):
		total = []
		PGA = self.getPGA()
		for i in PGA.values():
			total.append(i)
		tot = float(sum(total))
		tot = tot/len(total)
		return total

if __name__ == "__main__":
	print "do nothing yet"