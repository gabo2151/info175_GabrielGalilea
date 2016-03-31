# GUI para los encriptadores

from Tkinter import *
import string

# Metamos todo el codigo no mas, no hay tiempo de ver como importar
# Algo fallaba con el mio... usare el del ppt
def mainCrypt(word, jump):
	abcd = string.ascii_lowercase
	encrypt_word = ""
	for char in word:
		if char != " ":
			index = (abcd.index(char.lower()) + jump) % len(abcd)
			encrypt_word += abcd[index]
		else:
			encrypt_word += char
	return encrypt_word
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
# Resto del codigo

# Main window
window = Tk()
window.title("GUICrypt")
window.geometry("400x600")

# Etiqueta 1
labl1=Label(window, text="Escriba lo que desee encriptar")
labl1.place(x=10, y=10)

# Texto principal
texto_BOX = Text(window, height=25, width=53)
texto_BOX.place(x=10, y=30)

# Variables requeridas
opcion = IntVar()
opc = IntVar()
numero = StringVar()
num = IntVar()

# Nunca funciono pero lo dejo por si acaso
def callback():
	opc = opcion.get()
	num = int(numero.get())

# Opcion Cesar
OPT1 = Radiobutton(window, text="Cesar", variable=opcion, value=1, command=callback)
OPT1.place(x=10, y=420)

# Opcion Cenit-Polar
OPT2 = Radiobutton(window, text="Cenit-Polar", variable=opcion, value=2, command=callback)
OPT2.place(x=10, y=450)

# Num de saltos
numSpin = Spinbox(window, from_=0, to=26, textvariable=numero, command=callback)
numSpin.place(x=120, y=420)

# Boton
boton = Button(window, text="Haz lo tuyo", command=lambda:accionBoton())
boton.place(x=150, y=500)
def accionBoton():
	# Bueno... no se que pasa pero al menos funciona...
	# <meme: It's something>
	opc = opcion.get()
	num = int(numero.get())
	if opc == 1:
		textoDeBox = mainCrypt(texto_BOX.get("1.0",'end-1c'), int(num))
		texto_BOX.delete(1.0, END)
		texto_BOX.insert(END, textoDeBox)
	elif opc == 2:
		textoDeBox = mainCenPol(texto_BOX.get("1.0",'end-1c'))
		texto_BOX.delete(1.0, END)
		texto_BOX.insert(END, textoDeBox)
	else:
		texto_BOX.delete(1.0, END)
		texto_BOX.insert(END, "Elija una opcion")
# Intento de activar y desactivar el boton
#if texto_BOX.get("1.0",'end-1c') == "": boton.config(state=DISABLED)
#else: boton.config(state=NORMAL)


window.mainloop()