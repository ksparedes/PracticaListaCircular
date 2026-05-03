import ListasCirculares

clist=ListasCirculares.ListaCircular()

#Menu para lista enlazada circular    
def mostrarMenu2():
    print("1. Insertar al inicio")
    print("2. Insertar al final")
    print("3. Mostrar lista")
    print("4. Buscar elemento")
    print("5. Salir")
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
            v= input("Digite el valor a buscar ")
            if clist.search(v):
                print(f"El valor {v} se encuentra en la lista.")
            else:
                print(f"El valor {v} no se encuentra en la lista.")

        if op=="5":
            print("Saliendo...")
            break


