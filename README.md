# Reto No. 4:   "¿Descansando en Semana Universitaria?"
Resolver los siguientes problemas usando un notebook de python y subirlos a un repo:


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
   


2. Dada una cadena de longitud 1, determine si el código ASCII de primera letra de la cadena es par o no.

   ```pseudocode
   a : str
   b : int
   
   a = input("Ingrese un caracter: ")
   b = ord(a)

   if b%2 == 0:
      print("El código ASCII de la letra ", (a), " es ", (b), " sí es par.")
   else: 
      print("El código ASCII de la letra ", (a), " es ", (b), " no es par.")

   ```




3. Dado un carácter, construya un programa en Python para determinar si el carácter es un dígito o no.

   Los valores ASCII de { 0, 1, ..., 8, 9}   son   { 48, 49, ..., 56, 57 }, respectivamente.

   ```pseudocode
   a : str
   b : int
   
   a = input("Ingrese un caracter: ")
   b = ord(a)
   
   if b >= 48 and b <= 57:
      print("El caracter ", (a), " sí es un dígito.")
   else: 
      print("El caracter ", (a), " no es un dígito.")

   ```

   

4. Dado un número real x, construya un programa que permita determinar si el número es positivo, negativo o cero.
   Para cada caso de debe imprimir el texto que se especifica a continuación:

   Positivo: "El número x es positivo"
   Negativo: "El número x es negativo"
   Cero (0): "El número x es el neutro para la suma"


   ```pseudocode
   x : float
   x = float(input("Ingrese un número: "))
   
   if x > 0:
      print("El número ", x, " es positivo.")
     
   elif x < 0:
      print("El número ", x, " es negativo.")
  
   elif x == 0:
      print("El número ", x, " es el neutro para la suma.")

   ```




   
5. Dado el centro y el radio de un círculo, determinar si un punto de R2 pertenece o no al interior del círculo.


   ```pseudocode
   x : float
   y : float
   r : float
   
   x = float(input("Ingrese cordenada X del centro del círculo: "))
   y = float(input("Ingrese cordenada Y del centro del circulo: "))
   r = float(input("Ingrese el radio del círculo: "))
   
   x2 = float(input("Ingrese coordena X del punto: "))
   y2 = float(input("Ingrese coordena Y del punto: "))
   
   a = ((x2 - x) ** 2)
   b = ((y2 - y) ** 2)
   c = ((a + b) ** 0.5)
   
   if c < r or c == r:
      print("La coordenada ", x2, "," ,y2, " sí pertenece al interior del círculo.")
   else:
      print("La coordenada ", x2, "," ,y2, " no pertenece al interior del círculo.")

   ```




6. Dadas tres longitudes positivas, determinar si con esas longitudes se puede construir un triángulo.

   ```pseudocode
   a : float
   b : float
   c : float
   
   a = float(input("Ingrese la primera longitud: "))
   b = float(input("Ingrese la segunda longitud: "))
   c = float(input("Ingrese la tercera longitud: "))
   
   if a + b > c and a + c > b and b + c > a: 
      print("Con las 3 longitudes sí es posible formar un triangulo.")
   else:
      print("Con las 3 longitudes no es posible formar un triangulo.")

   ```



Notebook de Jupyter en archivo adjunto reto4.ipynb o acá:

https://colab.research.google.com/drive/1OVvz7fRnVKlxQzJ0nSfWFMbSdkN3tlWp?usp=sharing


