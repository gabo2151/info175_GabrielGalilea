# -*- coding: utf-8 -*-
def fibboPulento(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	elif n>1:
		return fibboPulento(n-1) + fibboPulento(n-2)

print fibboPulento( input("Ingrese el numero para calcular fibbonaci: ") )