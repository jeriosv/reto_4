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
