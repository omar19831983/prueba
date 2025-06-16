nombresProductos=[]
stocksProductos=[]
preciosProductos=[]

opcion="0"

"""
Agregar producto
Buscar producto
Actualizar cantidad/precio
Mostrar inventario completo
Eliminar producto
Salir
"""
def solicitarProducto():
    nombre=input("Ingrese el nombre del producto: ").lower()
    try:
        stock=int(input("Ingrese el stock del producto: "))
        precio=int(input("Ingrese el precio del producto: "))
        
        if stock<0 or precio <0:
            raise ValueError
            
        else:
            producto=[nombre,precio,stock]
            return producto

    except ValueError:
        print("Debe ingresar valores enteros positivos")
        
    
def guardarProducto(nombre,precio,stock):
    if nombre not in nombresProductos:
        nombresProductos.append(nombre)
        preciosProductos.append(precio)
        stocksProductos.append(stock)
        print("Se guardado correctamente el producto")
    else:
        print("No se puede guardar un producto con el mismo nombre que uno ya creado")

def buscarProducto(nombre):
    if nombre in nombresProductos:
        indice= nombresProductos.index(nombre)
        nombre=nombresProductos[indice]
        precio=preciosProductos[indice]
        stock=stocksProductos[indice]
        print("-"*60)
        print(f"Nombre: {nombre} \t Precio: ${precio} \t Stock: {stock} unidades")
        print("-"*60)
        #return [nombre,precio,stock]
        
    else:
        print("No existe un producto con ese nombre")

def actualizarProducto(nombre,nuevoPrecio,nuevoStock):
    if nombre in nombresProductos:
        indice= nombresProductos.index(nombre)
        stocksProductos[indice]=nuevoStock
        preciosProductos[indice]=nuevoPrecio
        print("Producto actualizado con éxito")
    else:
        print("No existe un producto con ese nombre")

def mostarInventarioCompleto():
    print("-"*60)
    if(len(nombresProductos)==0):
        print("Aún no hay productos agregados")
        return



    for indice in range(len(nombresProductos)):
        
        print(f"Nombre: {nombresProductos[indice]} \t Precio: ${preciosProductos[indice]} \t Stock: {stocksProductos[indice]} unidades")
    
    print("-"*60)



while opcion!="6":
    print("1.- Agregar producto")
    print("2.- Buscar producto")
    print("3.- Actualizar cantidad/precio")
    print("4.- Mostrar inventario completo")
    print("5.- Eliminar producto")
    print("6.- Salir")

    opcion=input("Ingrese la opción que desea(1-6): ")

    
    
    match opcion:

        case "1":
            nuevoProducto=solicitarProducto()#[nombre,precio,stock]
            if nuevoProducto != None:
                #guardarProducto(*nuevoProducto)
                guardarProducto(nuevoProducto[0],nuevoProducto[1],nuevoProducto[2])
        case "2":
            nombreProducto=input("Ingrese el nombre del producto a buscar: ").lower()
            buscarProducto(nombreProducto)
        case "3":
            print("*Ingrese los datos del producto a actualizar*")
            nuevoProducto=solicitarProducto()#[nombre,precio,stock]
            if nuevoProducto != None:
                actualizarProducto(*nuevoProducto)
        case "4":
            mostarInventarioCompleto()
        case "5":
            #crear el eliminar producto
            pass#el pass se debe borrar cuando coloquen el código correspondiente
        case "6":
            #salir...
            pass        

