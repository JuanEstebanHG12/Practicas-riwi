import csv
import os

class CRUD:
    def crear_archivo(self, archivo):
        if not os.path.exists(archivo):
            with open(archivo, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["id", "nombre", "edad"])


    def incrementar_id(self, archivo):
        with open(archivo, 'r') as file:
            filas = list(csv.reader(file))

        if len(filas) == 1:
            return 1
            
        ultimo_id = int(filas[-1][0])
        return ultimo_id + 1
    
    def crear(self, archivo, nombre, edad):
        id_nuevo = self.incrementar_id(archivo)
        with open(archivo , 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([id_nuevo, nombre, edad])
            return id_nuevo
    

    def listar(self, archivo):
        with open(archivo, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            return list(reader)
    
    def eliminar_por_id(self, archivo, id_eliminar):
        data = self.listar(archivo)
        for persona in data:
            if persona[0] == id_eliminar:
                data.remove(persona)
                self.sobreescribir(archivo, data)
                break
            
            
    def actualizar_por_id(self, archivo, id_actualizar, nombre= None, edad=None):
        data = self.listar(archivo)
        for persona in range(len(data)):
            if data[persona][0] == id_actualizar:
                if nombre is not None:
                    data[persona][1] = nombre
                    self.sobreescribir(archivo, data)
                    return f"Nombre Actualizada a {nombre}"
                
                if edad is not None:
                    data[persona][2] = edad
                    self.sobreescribir(archivo, data)
                    return f"Edad Actualizada a {edad}"
                break
            

    def sobreescribir(self, archivo, data):
        with open(archivo, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["id", "nombre", "edad"])
            for fila in data:
                writer.writerow(fila)

