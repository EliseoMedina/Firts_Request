'''
Hacer un programa que simule un cajero automatico con un saldo inicial de $1000
y tendra el siguiente menú de opciones:
'''

print("\n              Cajero Luffy")
input("Presione enter para continuar: ")

opcion = int(input("1. Ingresar dinero en la cuenta\n"
                   "2. Retirar dinero de la cuenta\n"
                   "3. Mostrar dinero de la cuenta\n"
                   "4. Salir\n"
                   "Seleccione una opcion: "))

saldo = 1000

if opcion == 1:
    cantidad = float(input("Ingrese la cantidad a depositar: "))
    saldo += cantidad
    print(f"Su saldo nuevo es de ${saldo} en su cuenta")

elif opcion == 2:
    cantidad = float(input("Ingrese la cantidad a retirar: "))
    if cantidad <= saldo:
        saldo -= cantidad
        print(f"Usted ha retirado ${cantidad} \nAhora tiene ${saldo} en su cuenta")
    else:
        print("Fondos insuficientes.")

elif opcion == 3:
    print(f"Usted tiene ${saldo} de saldo en su cuenta")
elif opcion == 4:
    print("Usted salió de su cuenta")
else:
    print("Error al seleccionar opción, intente de nuevo por favor.")
