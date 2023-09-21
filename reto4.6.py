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