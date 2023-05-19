while True:
    try:
        base = float(input("Ingresa la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        if base > 0 and altura > 0:
            break
        else:
            print("Los valores deben ser numéricos positivos. Inténtalo nuevamente.")
    except ValueError:
        print("Los valores deben ser numéricos. Inténtalo nuevamente.")


while True:
    try:
        lado1 = float(input("Ingresa la longitud de un lado: "))
        lado2 = float(input("Ingresa la longitud del segundo lado: "))
        lado3 = float(input("Ingresa la longitud del tercer lado: "))
        if lado1 > 0 and lado2 > 0 and lado3 > 0 and (lado1 == base or lado2 == base or lado3 == base):
            break
        else:
            print("Los valores deben ser numéricos positivos y uno de los lados debe ser igual a la base. Inténtalo nuevamente.")
    
    except ValueError:
        print("Uno de los valores ingresados no es válido. Inténtalo nuevamente.")


def calcular_area(base, altura):
    area = (base * altura) / 2
    return area

def calcular_perimetro(lado1, lado2, lado3):
    perimetro = (lado1 + lado2 + lado3)
    return perimetro

def clasificar_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        tipoTriangulo = "Equilátero"
        return tipoTriangulo
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipoTriangulo = "Isósceles"
        return tipoTriangulo
    else:
        tipoTriangulo = "Escaleno"
        return tipoTriangulo

area = calcular_area(base, altura)
perimetro = calcular_perimetro(lado1, lado2, lado3)
tipoTriangulo = clasificar_triangulo(lado1, lado2, lado3)


# Mostrar el resultado
print("El área del triángulo es: ", area, "El perimetro del triángulo es: ", perimetro, "El tipo de triángulo es: ", tipoTriangulo)
