lado1 = None
while lado1 == None and lado1 > 0:
    lado1 = int(input("Ingrese un lado del triangulo"))


lado2 = int(input("Ingrese un lado del triangulo"))
lado3 = int(input("Ingrese un lado del triangulo"))


# Numeros nulos, letras, negativos, verificación de condiciones, que el triangulo sea valido,


if lado1 ==  lado2 == lado3:
    print("Es equilatero"),
elif lado1 == lado2 and lado1 != lado3:
    print("es Isosceles")
else:
    print("Escaleno")
