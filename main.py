#Creando variables y ciclos en python
menuOpciones=0

#Pasos para crear una lista 
#1. Se crea la variable y se iguala a corchetes

listaProductos = []

while menuOpciones != 5:
    print("Bienvenido a bodegas JuanFE")
    print("**********************************")
    
    print("1. Digita 1 para agregar un producto a la bodega:")
    print("2. Digita 2 para ver todos los productos de la bodega:")
    print("3. Digita 3 para calcular el costo total de la bodega:")
    
    menuOpciones=int(input("\nDigita una opcion: "))

    if menuOpciones == 1:
        print("🛒Comenzaremos a registrar un producto:\n")

        #un pruducto es un dicionario (objeto)
        #Pasos para crear un diccionario
        #1. Creamos la variable utilizando llaves
        dicionarioProducto = {}
        #2. Agregamos valores y llaves al diccionario
        dicionarioProducto["id"]= int(input("Digita el id del producto:"))
        dicionarioProducto["nombre"]=input("Digita el nombre del producto:")
        dicionarioProducto["descripcion"]=input("Digita la descripcion del producto:")
        dicionarioProducto["precioUnitario"]=int(input("Digita el precio unitario del producto:"))
        dicionarioProducto["cantidadBodega"]=int(input("Digita la cantidad del producto en bodegas:"))
        dicionarioProducto["fotografia"]=input("Inserta la url de la fotografia del producto:")
        dicionarioProducto["marca"]=input("Digita la marca del producto:")
        #fotografia
        #marca
        #3. AGREGANDO UN DICCIONARIO A UNA LISTA
        listaProductos.append(dicionarioProducto)
        print("\n Exito agregando el producto 🤖 \n")

    elif menuOpciones == 2:
        print("📔Revisaremos nuestro inventario: \n")
    elif menuOpciones == 3:
        print("📊Estamos calculando: \n")
    else:
        print("👻Aun no contamos con esa opcion... \n")
    