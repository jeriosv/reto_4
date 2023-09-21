a : str
b : int

a = input("Ingrese un caracter: ")
b = ord(a)

if b%2 == 0:
  print("El código ASCII de la letra ", (a), " es ", (b), " sí es par.")
else: 
  print("El código ASCII de la letra ", (a), " es ", (b), " no es par.")