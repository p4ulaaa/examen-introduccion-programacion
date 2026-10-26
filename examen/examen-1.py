def consultar_saldo(saldo):
    print("Su saldo actual es de: ", saldo)
    return saldo

def retirar_dinero(saldo):
    cantidad = int(input("Ingrese la cantidad a retirar: "))
    if cantidad <= 0:
        print("Error. la cantidad que debe retirar debe ser mayor que cero.")
    elif cantidad > saldo:
        print("Error. no hay suficiente saldo")
    else:
        saldo = saldo - cantidad
        print("Retiro exitoso, saldo restante: ", saldo)
    return saldo

def depositar_dinero(saldo):
    cantidad = int(input("Ingrese la cantidad a depositar: "))
    if cantidad <= 0:
        print("Error. la cantidad a depositar debe ser mayor a cero.")
    else:
        saldo = saldo + cantidad
        print("Deposito exitoso, saldo restante: ", saldo)
    return saldo

saldo_inicial = 1000
opcion = -1

while opcion != 0:
    print("----- MENU -----")
    print("1. Consultar saldo. ")
    print("2. Depositar dinero. ")
    print("3. Retirar dinero. ")
    print("0. Salir. ")

    opcion = int(input("Ingrese una opcion: "))

    match opcion:
        case 1: saldo_inicial = consultar_saldo(saldo_inicial)
        case 2: saldo_inicial = depositar_dinero(saldo_inicial)
        case 3: saldo_inicial = retirar_dinero(saldo_inicial)
        case 0: print("Gracias por usar el cajero automatico. ")

    
