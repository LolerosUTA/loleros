
def suma (a, b):
    return (a + b)

def resta(a, b):
    return (a - b)
    
def multiplicacion (a, b):
    return (a * b)
    
def division (a, b):
    if b == 0:
            return " El resultado de la operacion no es valida"
    else:
            return (a / b)

print (" Bienvenido a la calculadora")
print(" 1. suma")
print(" 2. resta")
print(" 3. multiplicacion")
print(" 4. division")

opcion = input(" Seleccione la opcion 1/2/3/4 ")

num1 = int(input(" Ingrese primer numero:  "))
num2 = int(input(" Ingrese segundo numero: "))


if opcion == "1":
    print ( f" El valor de la suma es:", suma(num1, num2))
elif opcion == "2":
    print ( f" El valor de la resta es:",  resta(num1, num2))    
elif opcion == "3":
    print ( f" El valor de la multiplicacion es:", multiplicacion (num1, num2))
elif opcion == "4":
    print ( f" El valor de la division es:",  division(num1, num2))
else:
    print("opcion invalida")


        

         
    
    
    
