from funciones import lista

def modificarPyS():
    N = input("Ingrese nombre de la pelicula o serie: ")
    encontrado = False
    
    for i in range(len(lista)):
        if N == lista[i]["titulo"]:
            encontrado = True
            l = i
    if encontrado == True:
        print("Nombre encontrado: ", lista[l]["titulo"], ",", lista[l]["genero"], ",", lista[l]["productoras"], ",", lista[l]["tipo"], ",", lista[l]["estreno"], ",", lista[l]["valoracion"])
        print("     ")    
        elemento = input("¿Qué dato desea modificar? (Escriba el número del dato): \n1-titulo\n2-genero\n3-productora\n4-tipo\n5-año de estreno\n6-validacion de usuarios\n7-salir\nOpción: ")

        if elemento == '1':
            titulo = input("Ingrese nuevo título: ")
            lista[l]["titulo"] = titulo
            print(lista[l]["titulo"], ",", lista[l]["genero"], ",", lista[l]["productoras"], ",", lista[l]["tipo"], ",", lista[l]["estreno"], ",", lista[l]["valoracion"])

        elif elemento == '2':
            genero = input("Ingrese nuevo género: ")
            lista[l]["genero"] = genero
            print(lista[l]["titulo"], ",", lista[l]["genero"], ",", lista[l]["productoras"], ",", lista[l]["tipo"], ",", lista[l]["estreno"], ",", lista[l]["valoracion"])

        elif elemento == '3':
            productora = input("Ingrese nombre/s de la/s productora/s: ")
            lista[l]["productoras"] = productora
            print(lista[l]["titulo"], ",", lista[l]["genero"], ",", lista[l]["productoras"], ",", lista[l]["tipo"], ",", lista[l]["estreno"], ",", lista[l]["valoracion"])
            
        elif elemento == '4':
            tipo = input("Ingrese si es película o serie: ")
            lista[l]["tipo"] = tipo
            print(lista[l]["titulo"], ",", lista[l]["genero"], ",", lista[l]["productoras"], ",", lista[l]["tipo"], ",", lista[l]["estreno"], ",", lista[l]["valoracion"])

        elif elemento == '5':
            estreno = input("Ingrese año de estreno: ")
            lista[l]["estreno"] = estreno
            print(lista[l]["titulo"], ",", lista[l]["genero"], ",", lista[l]["productoras"], ",", lista[l]["tipo"], ",", lista[l]["estreno"], ",", lista[l]["valoracion"])
            
        elif elemento == '6':
            calificacion = input("Ingrese calificación de los usuarios: ")
            lista[l]["valoracion"] = calificacion
            print(lista[l]["titulo"], ",", lista[l]["genero"], ",", lista[l]["productoras"], ",", lista[l]["tipo"], ",", lista[l]["estreno"], ",", lista[l]["valoracion"])
        
        elif elemento == '7':
            print("fin de modificacion")

        else:
            print("No se halla en las opciones")

    else:
        print("no se halla en la lista")

def eliminarPYS():
    N = str(input("ingrese nombre de la pelicula o serie: "))
    encontrado = False
    for i in lista:
        if  N in i["titulo"]:
            encontrado = True
            l = i
    if encontrado == True:
        print("nombre encontrado: ",lista.index(l)+1, "-",l["titulo"],",",l["genero"],",",l["productoras"],",",l["tipo"],",",l["estreno"],",",l["valoracion"])

        elemento = input("¿lo desea eliminar?:\n1-si\n2-no\n3-salir\n*Opcion: ")
        if elemento == "1":#si
            lista.remove(l)
            print("eliminacion con exito")
            print(lista)

        elif elemento == "2": #no
            print("no se elimino elemento")

        elif elemento == "3": #salir
            print("volver al menu")

        else:
            print("error")

    else:
        print("no se halla en la lista")
