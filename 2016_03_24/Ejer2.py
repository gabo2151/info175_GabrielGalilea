import string

def encrypt(palabra, nuCod):
	palabra = palabra.lower()
	encoded = ""
	aBeCeDe = string.ascii_lowercase
	nABC = len(aBeCeDe)

	for i in range(0, len(palabra)):
		for j in range(0, nABC+1):
			if (j<nABC) and (palabra[i]==aBeCeDe[j]):
				if j+nuCod > nABC:
					rr = j+nuCod-nABC
					encoded += aBeCeDe[rr]
					break
				else:
					encoded += aBeCeDe[j+nuCod]
					break

			elif j == nABC:
				encoded += palabra[i]

	return encoded

if __name__ == "__main__":
	#print string.ascii_lowercase
	palabra = raw_input("Ingrese texto.\n")

	num = raw_input("Ingrese num de codificacion: ")
	if num: num = int(num)
	else: num = 0

	palabra = encrypt(palabra, num)

	print palabra