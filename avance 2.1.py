def tarjeta_bronce():
    compra = float(input("Dame el valor de tu última compra:"))
    puntos=compra*.10
    return("tienes",puntos,"puntos")

def tarjeta_plata():
    compra = float(input("Dame el valor de tu última compra:"))
    puntos=compra*.15
    return("tienes",puntos,"puntos")

def tarjeta_oro():
    compra = float(input("Dame el valor de tu última compra:"))
    puntos=compra*.20
    return("tienes",puntos,"puntos")
    

def menu():
    print("1-Tarjeta oro")
    print("2-Tarjeta plata")
    print("3-Tarjeta bronce")
    

def main():
    continua = True
    while continua:
        menu()
        opcion = int (input("Introduce una opcion:"))
        if opcion == 1:
           tarjeta_oro() 
        elif opcion == 2:
            tarjeta_plata()
        elif opcion == 3:
            tarjeta_bronce()
        elif opcion == 4:
            print("Usted no cuenta con una tarjeta participante")
            
        else:
            print("ERROR OPCION INVALIDA")
            continua  = False
main()
            

    