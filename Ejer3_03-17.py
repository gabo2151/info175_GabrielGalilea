# Codigo de Gabriel Galilea

if __name__ == "__main__":
	lista = []
	palabra = raw_input("Escriba una palabra:\n")
	while palabra:
		lista.append(palabra)
		palabra = raw_input("Escriba una palabra:\n")


	for i in lista:
		print i