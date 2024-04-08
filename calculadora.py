def calculator():
    print("Bienvenido a la Calculadora")
    print("Selecciona la operación que deseas realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    while True:
        # Pedir al usuario que elija una opción
        choice = input("Ingresa el número de la operación (1-5): ")

        # Verificar la opción elegida
        if choice == '1':
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            result = num1 + num2
            print(f"El resultado de {num1} + {num2} es: {result}")
        elif choice == '2':
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            result = num1 - num2
            print(f"El resultado de {num1} - {num2} es: {result}")
        elif choice == '3':
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            result = num1 * num2
            print(f"El resultado de {num1} * {num2} es: {result}")
        elif choice == '4':
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            if num2 == 0:
                print("Error: No se puede dividir entre cero.")
            else:
                result = num1 / num2
                print(f"El resultado de {num1} / {num2} es: {result}")
        elif choice == '5':
            print("¡Adiós!")
            break
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    calculator()