from sumar import sumar
from resta import restar
from multiplicar import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

def menu():
    print("Seleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Suma avanzada")
    print("6. Salir")

def main():
    while True:
        menu()
        choice = input("Ingrese una opción (1/2/3/4/5/6): ")
        
        if choice == '1':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print(f"Resultado: {sumar(num1, num2)}")
        
        elif choice == '2':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print(f"Resultado: {restar(num1, num2)}")
        
        elif choice == '3':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print(f"Resultado: {multiplicar(num1, num2)}")
        
        elif choice == '4':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            if num2 == 0:
                print("Error: División por cero no permitida")
            else:
                print(f"Resultado: {dividir(num1, num2)}")
        
        elif choice == '5':
            numeros = input("Ingrese los números separados por espacios: ")
            numeros_list = list(map(float, numeros.split()))
            print(f"Resultado: {suma_avanzada(numeros_list)}")
        
        elif choice == '6':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
