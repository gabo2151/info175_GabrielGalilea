# Codigo de Gabriel Galilea

def funcQuePide2Numeros(x, y):
	if x > y:
		return x+" es mayor que "+y
	elif x < y:
		return x+" es menor que "+y
	else:
		return x+" e "+y+" son iguales"

if __name__ == "__main__":
	x = raw_input("Ingrese numero 1: ")
	y = raw_input("Ingrese numero 2: ")

	print( funcQuePide2Numeros(x, y) )