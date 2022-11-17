import random, sys
derrota = ("Perdiste")
def pedir_dificultad():
    while True:
        print("""Seleccione dificultad: 1= Simple
                       2= Intermedio
                       3= Avanzado
                       4= Experto
                       5= Personalizado (establece los limites)
                       6= Que juegue la IA""")
        dificultad = input("Que dificultad desea: ")
        try: 
            dificultad = int(dificultad)
        except:
            print("Porfavor, selccione una dificultad introduciendo un numero del 1 al 4")
            pass
        else:
            intentos = 0
            if dificultad == 1:
                numero1 = random.randint(0, 100)
                print("Tu numero esta entre 0 y 100")
                while intentos < 3:
                    intento = input("Diga el numero:")
                    try: 
                        intento = int(intento)
                    except:
                        print("Introduzca un numero porfavor")
                        pass
                    else:
                        if intento < 0:
                            print("El numero tiene que ser mayor que 0")
                            continue
                        elif intento > 100:
                            print("El numero tiene que ser menor que 100")
                            continue
                        else:
                            if intento == numero1:
                                print("Acertaste")
                                break
                            elif intento > numero1:
                                print("El numero es mas pequeno")
                                intentos +=1
                                continue
                            elif intento < numero1:
                                print("El numero es mas grande")
                                intentos +=1
                                continue
            elif dificultad == 2:
                numero2 = random.randint(0, 1000)
                print("Tu numero esta entre 0 y 1000")
                while intentos < 3:
                    intento = input("Diga el numero:")
                    try: 
                        intento = int(intento)
                    except:
                        print("Introduzca un numero porfavor")
                        pass
                    else:
                        if intento < 0:
                            print("El numero tiene que ser mayor que 0")
                            continue
                        elif intento > 1000:
                            print("El numero tiene que ser menor que 1000")
                            continue
                        else:
                            if intento == numero2:
                                print("Acertaste")
                                break
                            elif intento > numero2:
                                print("El numero es mas pequeno")
                                intentos +=1
                                continue
                            elif intento < numero2:
                                print("El numero es mas grande")
                                intentos +=1
                                continue
            elif dificultad == 3:
                numero3 = random.randint(0, 1000000)
                print("Tu numero esta entre 0 y 1000000")
                while intentos < 3:
                    intento = input("Diga el numero:")
                    try: 
                        intento = int(intento)
                    except:
                        print("Introduzca un numero porfavor")
                        pass
                    else:
                        if intento < 0:
                            print("El numero tiene que ser mayor que 0")
                            continue
                        elif intento > 1000000:
                            print("El numero tiene que ser menor que 1000000")
                            continue
                        else:
                            if intento == numero3:
                                print("Acertaste")
                                break
                            elif intento > numero3:
                                print("El numero es mas pequeno")
                                intentos +=1
                                continue
                            elif intento < numero3:
                                print("El numero es mas grande")
                                intentos +=1
                                continue
            elif dificultad == 4:
                numero4 = random.randint(0, 1000000000000)
                print("Tu numero esta entre 0 y 100000000000")
                while intentos < 3:
                    intento = input("Diga el numero:")
                    try: 
                        intento = int(intento)
                    except:
                        print("Introduzca un numero porfavor")
                        pass
                    else:
                        if intento < 0:
                            print("El numero tiene que ser mayor que 0")
                            continue
                        elif intento > 1000000000000:
                            print("El numero tiene que ser menor que 100000000000")
                            continue
                        else:
                            if intento == numero4:
                                print("Acertaste")
                                break
                            elif intento > numero4:
                                print("El numero es mas pequeno")
                                intentos +=1
                                continue
                            elif intento < numero4:
                                print("El numero es mas grande")
                                intentos +=1
                                continue
            elif dificultad == 5:
                minimo = input("Cual es el numero menor: ")
                try:
                    minimo = int(minimo)
                    """print(type(minimo))"""
                except:
                    print("Escriba un numero")
                    pass
                else:
                    maximo = input("Cual es el numero mayor: ")
                    try:
                        maximo = int(maximo)
                    except:
                        print("Escriba un numero")
                        pass
                    else:
                        numero5 = random.randint(minimo, maximo)
                        print("Tu numero esta entre {} y {}".format(minimo, maximo))
                        while intentos < 3:
                            intento = input("Diga el numero: ")
                            try: 
                                intento = int(intento)
                            except:
                                print("Introduzca un numero porfavor")
                                pass
                            else:
                                if intento < minimo:
                                    print("El numero tiene que ser mayor que",minimo)
                                    continue
                                elif intento > maximo:
                                    print("El numero tiene que ser menor que",maximo)
                                    continue
                                else:
                                    if intento == numero5:
                                        print("Acertaste")
                                        break
                                    elif intento > numero5:
                                        print("El numero es mas pequeno")
                                        intentos +=1
                                        continue
                                    elif intento < numero5:
                                        print("El numero es mas grande")
                                        intentos +=1
                                        continue 
            elif dificultad == 6:
                   
            else:
                print("Introduzca un numero de entre el 1 y el 4")
                pass

"""def juego():
    intentos = 0
    if dificultad == 1:
        while intentos < 3:
            print(" Tu numero esta entre 0 y 100")
            intento = input("Diga el numero:")
            try: 
                intento = int(intento)
            except:
                print("Introduzca un numero porfavor")
                pass
            else:
                if intento < 0:
                    print("El numero tiene que ser mayor que 0")
                    pass
                elif intento > 100:
                    print("El numero tiene que ser menor que 100")
                    pass
                else:
                    if intento == numero1:
                        print("Acertaste")
                        break
                    elif intento > numero1:
                        print("El numero es mas pequeno")
                        intentos +=1
                        pass
                    elif intento < numero1:
                        print("El numero es mas grande")
                        intentos +=1
                        pass"""
pedir_dificultad()
