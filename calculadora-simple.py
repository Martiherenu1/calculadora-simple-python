#CALCULADORA SIMPLE EN CONSOLA

def suma(a, b):
    return a+b

def resta(a, b):
    return a-b

def multiplicacion(a, b):
    return a*b

def division(a, b):
    return a/b

def modulo(a, b):
    return a%b


def potencia(a, b):
    return a**b

opcion = -1

while opcion != 0:

    print("1. SUMA")
    print("2. RESTA")
    print("3. MULTIPLICACION")
    print("4. DIVISION")
    print("5. MODULO")
    print("6. POTENCIA")
    operacion = int(input("Ingrese la operacion a realizar: "))

    num1 = int(input("Ingrese el primer numero:"))
    num2 = int(input("Ingrese el segundo numero:"))

    if operacion == 1:
        print(f"RESULTADO: {suma(num1, num2)}")
    elif operacion == 2:
        print(f"RESULTADO: {resta(num1, num2)}")
    elif operacion == 3:
        print(f"RESULTADO: {multiplicacion(num1, num2)}")
    elif operacion == 4:
        print(f"RESULTADO: {division(num1, num2)}")
    elif operacion == 5:
        print(f"RESULTADO: {modulo(num1, num2)}")
    elif operacion == 6:
        print(f"RESULTADO: {potencia(num1, num2)}")

    opcion = int(input("Quiere hacer otro calculo? 1 SI - 0 NO:"))
