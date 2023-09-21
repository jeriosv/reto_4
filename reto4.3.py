a : str
b : int

a = input("Ingrese un caracter: ")
b = ord(a)

if b >= 48 and b <= 57:
  print("El caracter ", (a), " sí es un dígito.")
else: 
  print("El caracter ", (a), " no es un dígito.")
