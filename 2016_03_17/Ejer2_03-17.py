# Codigo de Gabriel Galilea

if __name__ == "__main__":
	lista = ""
	palabra = raw_input("Escriba una palabra:\n")
	while palabra:
		palabra = palabra.upper()
		palabra += "\n"
		lista += palabra
		palabra = raw_input("Escriba una palabra:\n")

	print lista