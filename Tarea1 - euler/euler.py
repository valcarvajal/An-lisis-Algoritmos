import sys

sys.setrecursionlimit(1000000000)

def e_lineal(n):
	factorial = 1;
	e = 1	#euler
	for j in range(1, n):
		factorial *= j
		e += 1 / factorial
	return e

def factorial(n):
	if n == 0:
		return 1
	if n > 1:
		return n * factorial(n - 1)
	return n

def e_cuadratica(n):
	e = 0
	for j in range(n):
		e += 1 / factorial(j)
	return e

