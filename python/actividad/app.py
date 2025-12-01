from crud import CRUD
from crud_json import JSON

crud = CRUD()
crud_json = JSON()
archivo = "datos.csv"
archivo_json = "datos.json"
crud.crear_archivo(archivo)
crud_json.crear_archivo_json(archivo_json)

while True:
    print("----MENU----")
    print("1.Crear persona")
    print("2.Listar Personas")
    print("3.Eliminar")
    print("4.Actuaizar")
    print("5.Salir")

    opcion = input("ingresar una opcion: ")

    if opcion == "1":
        nombre = input("Ingresar Nombre: ")
        edad = input("Ingresar edad: ")
        id_creado = crud.crear(archivo, nombre, edad)
        crud_json.crear_persona_json(archivo_json, nombre , edad)
        print(f"Persona creada con Id -> {id_creado}")

    elif opcion == "2":
        datos = crud.listar(archivo)
        for dato in datos:
            print(f"ID: {dato[0]}| Nombre: {dato[1]}| Edad: {dato[2]}")
            
        datos_json = crud_json.load_data_json(archivo_json)
        print("Listado desde JSON")
        for dato in datos_json:
            print(f"ID: {dato['id']}| Nombre: {dato['nombre']}| Edad: {dato['edad']}")
    
    elif opcion == "3":
        print("Eliminar")
        id_eliminar = input("Que ID desea eliminar?: ")
        crud.eliminar_por_id(archivo, id_eliminar)

    elif opcion == "4":
        id_actualizar = input("Que ID desea actualizar?: ")
        print("1-Actializar nombre: ")
        print("2-Actializar edad: ")
        while True:
            opcion = input("Ingresar opcion: ")
            if opcion == '1':
                nuevo_nombre = input("ingresar nuevo nombre: ")
                print(crud.actualizar_por_id(archivo, id_actualizar, nombre=nuevo_nombre))
                print(crud_json.modificar_datos(archivo_json,id_actualizar, nombre=nuevo_nombre))
                break
            elif opcion == '2':
                nueva_edad = input("ingresar nueva edad: ")
                print(crud.actualizar_por_id(archivo, id_actualizar, edad=nueva_edad))
                print(crud_json.modificar_datos(archivo_json,id_actualizar, edad=nueva_edad))
                break
            else:
                print("Ingresar opcion valida")
    elif opcion == "5":
        print("Saliendo")
        break
    else:
        print("opcion no existe")