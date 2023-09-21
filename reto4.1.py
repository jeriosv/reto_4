n : int 
n = int(input("Ingrese un número entero: ")) # Conversión a entero

if n == 97 or n == 101 or n == 105 or n == 111 or n == 117:
  print( (n), " sí es una vocal minúscula.")
else:
  print( (n), " no es una vocal minúscula.")

print("El número ", (n), " corresponde al código ASCII: ", chr(n))