#// Control de gastos personales //

gastos = []

while True: #// Bucle infinito //
    print("\n Control de Gastos Personales")
    print("1. Agregar gasto")
    print("2. Ver gastos")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")  #//Escuchamos al usuario para que elija una opción (input)//
    if opcion == "1":
        monto = float(input("Ingrese el monto del gasto: "))  #//Solicitamos al usuario que ingrese el monto del gasto (input+flolat)//
        categoria = input("Ingrese la categoría del gasto: ")  #//Solicitamos al usuario que ingrese la categoría del gasto (input)//
        descripcion = input("Ingrese la descripción del gasto: ")  #//Solicitamos al usuario que ingrese la descripción del gasto (input)//
        #//Agregamos el gasto a la lista de gastos (append)//
        gastos.append({
            "categoria": categoria,
            "descripcion": descripcion,
            "monto": monto
        })
        with open("gastos.txt", "a") as archivo:  #//Abrimos el archivo gastos.txt en modo de agregar (append)// Tener en cuenta que el "a" es para agregar al final del archivo sin borrar lo que ya hay//
            archivo.write(f"{categoria}, {descripcion}, {monto}\n")
        print("Gasto agregado.")
        
    elif opcion == "2":
        categorias = {}
        
        for g in gastos: #// nombro g) a cada gasto dentro de la lista 
        
            if g["categoria"] in categorias:
                categorias[g["categoria"]] += g["monto"]
            else: 
                categorias[g["categoria"]] = g["monto"]
    #Fuera
        for cat, total_gastos in categorias.items():
                print(cat, ":", total_gastos)
        
        
    elif opcion == "3":
        print("Saliendo del programa.")
        break  #// Aqui se rompe el bucle y se finaliza el programa// (Es un sal del "While" ya mismo) 
                #// Tener en cuena que el brak es como un boton de salida de emergencia//
    
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")
        