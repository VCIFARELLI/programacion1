from funciones import imprimlistado
from funciones import buscarPyS
from funciones import agregarPyS
from funciones import listar
from funciones2 import modificarPyS
from funciones2 import eliminarPYS


def menuPrincipal():
        print("Elija una opcion del siguiente menu:(escriba el numero)")
        print('1)- lista de peliculas y series')
        print('2)- buscar pelicula o serie')
        print('3)- modificar pelicula o serie')
        print('4)- agregar pelicula o serie')
        print('5)- listas segun genero/tipo/valoracion/estreno')
        print('6)- eliminar pelicula o serie')
        print('7)- salir ')
        eleccion = int(input("elijo la opcion: "))                

        while (eleccion != 0):
                if eleccion == 1:
                        imprimlistado()
                        print("=====================================================")
                        menuPrincipal()
                
                        break
                elif eleccion == 2:
                        buscarPyS()
                        print("=====================================================")
                        menuPrincipal()
                        break
                elif eleccion == 3:
                        modificarPyS()
                        print("=====================================================")
                        menuPrincipal()
                        break
                elif eleccion == 4:
                        agregarPyS()
                        print("=====================================================")
                        menuPrincipal()
                        break
                elif eleccion == 5:
                        listar()
                        print("=====================================================")
                        menuPrincipal()
                        break
                elif eleccion == 6:
                        eliminarPYS()
                        print("=====================================================")
                        menuPrincipal()
                        break
                elif eleccion == 7:
                        print("Gracias por sus consultas, que disfrute su tiempo")
                        break

                else:
                        print('opcion no valida')
                        print("=====================================================")
                        menuPrincipal()
                        break         
menuPrincipal()
             
        