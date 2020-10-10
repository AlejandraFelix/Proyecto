import random

def tarjeta_bronce():
    print("Dame el valor de tu última compra:")
    compra = abs(float(input()))
    puntos=compra*.10
    if compra >= 500:
        n = random.randint(1,10)
        print("se te sumaron",n,"puntos")
        print("tienes",puntos+n,"puntos")
    
    else:
        print("no sumaste puntos porque tu compra fue menor a $500")

def tarjeta_plata():
    print("Dame el valor de tu última compra:")
    compra = abs(float(input()))
    puntos=compra*.15
    if compra >= 500:
        n = random.randint(1,10)
        print("se te sumaron",n,"puntos")
        print("tienes",puntos+n,"puntos")
        
    else:
        print("no sumaste puntos porque tu compra fue menor a $500")
    

def tarjeta_oro():
    print("Dame el valor de tu última compra:")
    compra = abs(float(input()))
    puntos=compra*.20
    if compra >= 500:
        n = random.randint(1,10)
        print("se te sumaron",n,"puntos")
        print("tienes",puntos+n,"puntos")
        
    else:
        print("no sumaste puntos porque tu compra fue menor a $500")

    
lista_beneficios_oro = ["descuentos","premios","meses sin intereses","promociones"]
 
lista_beneficios_plata = ["promociones","descuentos","meses sin intereses"]

lista_beneficios_bronce = ["promociones","meses sin intereses"]

def menu():
    print("1-Tarjeta oro",lista_beneficios_oro)
    print("2-Tarjeta plata",lista_beneficios_plata)
    print("3-Tarjeta bronce",lista_beneficios_bronce)
    
#En esta parte estoy utilizando ciclos
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
            print("Saca tu tarjeta participante")
            
           
        else:
            print("ERROR OPCION INVALIDA")
            continua  = False
main()
            

    