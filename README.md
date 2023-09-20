# Reto No. 4:   "Descansando en Semana Universitaria"
Resolver los siguientes problemas usando un notebook de python y subirlos a un repo.

1. Dado un número entero, determinar si ese número corresponde al código ASCII de una vocal minúscula.

   Los valores ASCII de { a, e, i, o, u }   son   { 97, 101, 105, 111, 117 }, respectivamente.

   ```pseudocode
   n : int 
   n = int(input("Ingrese un número entero: ")) # Conversión a entero

   if n == 97 or n == 101 or n == 105 or n == 111 or n == 117:
      print( (n), " sí es una vocal minúscula.")
   else:
      print( (n), " no es una vocal minúscula.")

   print("El número ", (n), " corresponde al código ASCII: ", chr(n))
   ```
   

3. Dada una cadena de longitud 1, determine si el código ASCII de primera letra de la cadena es par o no.

4. Dado un carácter, construya un programa en Python para determinar si el carácter es un dígito o no.

5. Dado un número real x, construya un programa que permita determinar si el número es positivo, negativo o cero.
   Para cada caso de debe imprimir el texto que se especifica a continuación:

   Positivo: "El número x es positivo"
   Negativo: "El número x es negativo"
   Cero (0): "El número x es el neutro para la suma"
   
6. Dado el centro y el radio de un círculo, determinar si un punto de R2 pertenece o no al interior del círculo.

7. Dadas tres longitudes positivas, determinar si con esas longitudes se puede construir un triángulo.
