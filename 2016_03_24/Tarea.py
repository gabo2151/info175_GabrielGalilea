# GUI para los encriptadores

from Tkinter import *
import string

# Metamos todo el código no más, no hay tiempo de ver como importar
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
def mainCrypt(text, num):
	palabra = encrypt(text, num)
	return palabra
# Metodo mio (lamentable implementacion pero es lo que tengo) de CenitPolar
def t_cenit(t):
	t = t.replace("C", "P")
	t = t.replace("c", "p")
	t = t.replace("E", "O")
	t = t.replace("e", "o")
	t = t.replace("N", "L")
	t = t.replace("n", "l")
	t = t.replace("I", "A")
	t = t.replace("i", "a")
	t = t.replace("T", "R")
	t = t.replace("t", "r")
	return t
def t_polar(t):
	t = t.replace("P", "C")
	t = t.replace("p", "c")
	t = t.replace("O", "E")
	t = t.replace("o", "e")
	t = t.replace("L", "N")
	t = t.replace("l", "n")
	t = t.replace("A", "I")
	t = t.replace("a", "i")
	t = t.replace("R", "T")
	t = t.replace("r", "t")
	return t
def mainCenPol(text):
	result = ""
	for t in text:
		if t=="C" or t=="c" or t=="E" or t=="e" or t=="N" or t=="n" or t=="I" or t=="i" or t=="T" or t=="t":
			t = t_cenit(t)

		elif t=="P" or t=="p" or t=="O" or t=="o" or t=="L" or t=="l" or t=="A" or t=="a" or t=="R" or t=="r":
			t = t_polar(t)

		result += t
	return result
# Resto del código

window = Tk()
window.title("GUICrypt")

window.geometry("400x600")

window.mainloop()