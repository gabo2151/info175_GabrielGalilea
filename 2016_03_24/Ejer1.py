# Devuelve un listado de numeros que son divisibles por
# 3 y 7 a la vez (Desde 0 hasta el numero ingresado)

def multiplo (num):
	if (num%3)!=0 or (num%7)!=0:
		return False
	else:
		return True

if __name__ == "__main__":
	ent = int(raw_input("Ingresa un numero\n"))

	lista = []
	for x in range(0, ent):
		if multiplo(x):
			lista.append(x)

	print lista