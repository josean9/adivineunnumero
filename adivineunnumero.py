import random 
import sys

numero2 = random.randint(0, 100)
def pedir_dificultad():
    while True:
        print("""Seleccione dificultad: 1= Simple
                                        2= Intermedio
                                        3= Avanzado
                                        4= Experto""")
        dificultad = input("Que dificultad desea: ")
        try: 
            dificultad = int(dificultad)
        except:
            pass
        else:
            if dificultad == 1:
                continue
            elif dificultad == 2:
                continue
            elif dificultad == 3:
                continue
            else:
                break
    return("Ha seleccionado la dificultad",dificultad)
pedir_dificultad()
