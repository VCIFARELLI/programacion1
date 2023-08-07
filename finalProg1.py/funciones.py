
lista = [
        {"titulo":"titanic","genero":"romance/drama","productoras":"20th Century Studios, Paramount Pictures, Lightstorm Entertainment","tipo":"Pelicula","estreno":"1998","valoracion": "7.0"},
        {"titulo":"el niño que domó el viento","genero":"drama","productoras":"Participant Media/Netflix","tipo":"Pelicula","estreno":"2019","valoracion":"7.0"},
        {"titulo":"hotel transylvania","genero":"infantil/comedia","productoras":"Sony Pictures Animation, Columbia Pictures, Happy Madison","tipo":"Pelicula","estreno":"2012","valoracion":"6,0"},
        {"titulo":"el secreto de sus ojos","genero":"suspenso/crimen","productoras":"Coproducción Argentina-España; 100 Bares, Haddock Films, Telefé, Canal+ España","tipo":"Pelicula","estreno":"2009","valoracion":"8.0"},
        {"titulo":"barbie","genero":"Comedia/Drama","productoras":"Mattel, LuckyChap Entertainment, Mattel Films, Heyday Films, NB/GG Pictures","tipo":"Pelicula","estreno":"2023","valoracion":"7.0"},
        {"titulo":"caleidoscopio","genero":"Drama/Acción(Robo)","productoras":"Automatik Entertainment, Scott Free Productions, Netflix.","tipo":"Serie","estreno":"2023","valoracion":"6.0"},
        {"titulo":"la casa de papel","genero":"Intriga/Acción (Robos y Atracos)","productoras":"Vancouver Media, Atresmedia Televisión. Distribuidora: Netflix.","tipo":"Serie","estreno":"2017","valoracion":"7.0"},
        {"titulo":"breaking bad","genero":"Drama (Drogas. Enfermedad. Policíaco)","productoras":"Gran Via Productions, High Bridge Productions, Sony Pictures Television","tipo":"Serie","estreno":"2008","valoracion":"9.0"},
        {"titulo":"las chicas gilmore","genero":"Comedia/Drama (Familia. Adolescencia)","productoras":"Dorothy Parker Drank Here Productions, Hofflund/Polone Production, Warner Bros. Television","tipo":"Serie","estreno":"2000","valoracion":"6.0"},
        {"titulo":"rebelde way","genero":"Drama/Comedia/Romance (Adolescencia. Colegios y Universidad)","productoras":"Cris Morena Group S.A, Yair Dori Communications","tipo":"Serie","estreno":"2002","valoracion":"3.0"}
        ]

def imprimlistado(): #punto3)
    for i in lista:
        print(lista.index(i)+1,":",i["titulo"],",",i["genero"],",",i["productoras"],",",i["tipo"],",",i["estreno"],",",i["valoracion"])
    

def agregarPyS():#punto4)
    nuevoPyS= {"titulo": "", "genero": "", "productoras": "","tipo": "", "estreno": "", "valoracion": ""}
    nuevoPyS["titulo"] = str(input("ingrese titulo: "))
    nuevoPyS["genero"]=str(input("ingrese genero: "))
    nuevoPyS["productoras"] =str(input("ingrese nombre de productoras/compañias: "))
    nuevoPyS["tipo"] =str(input("ingrese tipo(serie o pelicula): "))
    nuevoPyS["estreno"] =str(input("ingrese año de estreno: "))
    nuevoPyS["valoracion"] =str(input("ingrese valoracion del usuario (numeros separados por punto, ejemplo x.z): "))
    lista.append(nuevoPyS)
    print(lista)
    
 
def buscarPyS(): #punto 5)
    N = str(input("ingrese nombre de la pelicula o serie: "))
    encontrado = False
    for i in lista:
        if  N in i["titulo"]:
            encontrado = True
            l = i
    if encontrado == True:
        print("nombre encontrado: ",lista.index(l)+1, "-",l["titulo"],",",l["genero"],",",l["productoras"],",",l["tipo"],",",l["estreno"],",",l["valoracion"])
    else:
        print("no se halla en la lista")
 

def listar(): #punto7 (por genero,tipo,valoracion)
    elemento = str(input("¿como desea listar? (Escriba el número del dato): \n1-genero\n2-tipo\n3-valoracion de usuarios\n4-estreno\n5-salir\nOpción: "))
    for i in lista:
        if elemento == "1":#todas
            for i in lista:
                print(lista.index(i)+1,":",i["titulo"],"----->",i["genero"])
                print("-----------------------------------------------------------------------------")

            genero =input("Ingrese que genero busca (Escriba el número del dato): \n1-drama\n2-accion\n3-comedia\n4-suspenso\n5-intriga\n6-romance\n7-salir\nopcion: ")
            if genero == "1": #drama
                print("la/s pelicula/s o serie/s de Drama son: ")
                print("1-",lista[0]["titulo"])
                print("2-",lista[1]["titulo"])
                print("3-",lista[4]["titulo"])
                print("4-",lista[5]["titulo"])
                print("5-",lista[7]["titulo"])
                print("6-",lista[8]["titulo"])
                print("7-",lista[9]["titulo"])
                break

            elif genero == "2":#accion
                print("la/s pelicula/so serie/s de Accion son: ")
                print("1-",lista[5]["titulo"])
                print("2-",lista[6]["titulo"])
                break
                    
            elif genero == "3":#comedia
                print("la/s pelicula/s o serie/s de Comedia son: ")
                print("1-",lista[2]["titulo"])
                print("2-",lista[4]["titulo"])
                print("3-",lista[8]["titulo"])
                print("4-",lista[9]["titulo"])
                break

            elif genero == "4":#suspenso
                print("la/s pelicula/s o serie/s de Suspenso son: ")
                print("1-",lista[3]["titulo"])
                break

            elif genero == "5":#intriga
                print("la/s pelicula/s o serie/s de Intriga son: ")
                print("1-",lista[6]["titulo"])
                break

            elif genero == "6":#romance
                print("la/s pelicula/s o serie/s de Romance son: ")
                print("1-",lista[0]["titulo"])
                print("1-",lista[9]["titulo"])
                break

            elif genero == "7":#salir
                print("gracias por su consulta")
                break
            else:
                print("error")
                break

        elif elemento == "2": #tipo
                tipo =str(input("Ingrese que tipo busca:\n1-pelicula\n2-serie\n3-salir\n-opcion: "))
                if tipo == "1":
                    print("PELICULAS:")
                    print("*",lista[0]["titulo"])
                    print("*",lista[1]["titulo"])
                    print("*",lista[2]["titulo"])
                    print("*",lista[3]["titulo"])
                    print("*",lista[4]["titulo"])
                    break

                elif tipo == "2":
                    print("SERIES:")
                    print("*",lista[5]["titulo"])
                    print("*",lista[6]["titulo"])
                    print("*",lista[7]["titulo"])
                    print("*",lista[8]["titulo"])
                    print("*",lista[9]["titulo"])
                    break

                elif tipo == "3":
                    print("gracias por su consulta")
                    break

                else:
                    print("error")
                    break

        elif elemento == "3": #valoracion
                print(lista.index(i)+1,":",i["titulo"],"----->",i["valoracion"])
                

        elif elemento == "4": #estreno
                print(lista.index(i)+1,":",i["titulo"],"----->",i["estreno"])
                

        elif elemento == "5":
                print("fin")
                break

        else:
                print("error")
                break





