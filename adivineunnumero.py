import random, sys
numero1 =random.randint(0, 100)
numero2 = random.randint(0, 1000)
numero3 = random.randint(0, 1000000)
numero4 = random.randint(0, 1000000000000)
def pedir_dificultad():
    while True:
        print("""Seleccione dificultad: 1= Simple
                       2= Intermedio
                       3= Avanzado
                       4= Experto""")
        dificultad = "2"
        #dificultad = input("Que dificultad desea: ")
        try: 
            dificultad = int(dificultad)
        except:
            print("Porfavor, selccione una dificultad introduciendo un numero del 1 al 4")
            pass
        else:
            if dificultad == 1:
                print("Ha seleccionado la dificultad facil")
                break
            elif dificultad == 2:
                print("Ha seleccionado la dificultad intermedia")
                break
            elif dificultad == 3:
                print("Ha seleccionado la dificultad avanzado")
                break
            elif dificultad == 4:
                print("Ha seleccionado la dificultad experto")
                break
            else:
                print("Seleccione un numero del 1 al 4")
                pass
def juego():
    intentos = 0
    if dificultad == 1:
        while
    elif dificultad == 2:
    elif dificultad == 3:
    elif dificultad == 4:
pedir_dificultad()
juego()