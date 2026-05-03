import ListasCirculares

clist=ListasCirculares.ListaCircular()

#Menu para lista enlazada circular    
def mostrarMenu2():
    print("1. Insertar al inicio")
    print("2. Insertar al final")
    print("3. Mostrar lista")
    print("4. Buscar elemento")
    print("5. Eliminar primer elemento")
    print("6. Eliminar por valor")
    print("7. Tamaño de la lista")
    print("8. Invertir lista")
    print("9. Ordenar lista")
    print("10. Salir")
    print("------------------------------------")

def mainCircular():
    while True:
        mostrarMenu2()

        op=input("Digite su opción " )
        print(" ")
        if op=="1":
            data = input("Digite el valor a insertar: ")
            clist.insert_at_first(data)


        if op=="2":
            data = input("Digite el valor a insertar: ")
            clist.insert_at_end(data)

        if op=="3":
            clist.display()

        if op=="4":
            k= input("Digite el valor a buscar ")
            clist.search(k)

        if op=="5":
            clist.delete_first()

        if op=="6":
            k = input("Digite el valor a eliminar: ")
            clist.delete_value(k)

        if op=="7":
            print("Tamaño de la lista:", clist.mostrarTam())

        if op=="8":
            clist.reverse()

        if op=="9":
            clist.sort()

        if op=="10":
            print("Saliendo...")
            break
