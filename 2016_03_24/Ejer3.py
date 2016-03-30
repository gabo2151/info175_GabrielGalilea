#CENIT
#POLAR
import string

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

def cenPol(text):
	result = ""
	for t in text:
		if t == "C" or "c" or "E" or "e" or "N" or "n" or "I" or "i" or "T" or "t":
			print "entro a cenit " + t
			t = t_cenit(t)

		elif t == "P" or "p" or "O" or "o" or "L" or "l" or "A" or "a" or "R" or "r":
			print "entro a polar"
			t = t_polar(t)

		result += t
	return result

if __name__ == "__main__":
	text = ""
	while len(text) == 0:
		text = raw_input("Escriba lo que desee encriptar:\n")

	print cenPol(text)