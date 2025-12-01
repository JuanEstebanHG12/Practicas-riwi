import json
import os

class JSON:
    
    def crear_archivo_json(self, archivo):
        if not os.path.exists(archivo):
            with open(archivo, 'w') as file:
                json.dump([], file, indent=4)
                
    def crear_persona_json(self, archivo, nombre, edad):
        nuevo_id = self.incrementar_id(archivo)
        data = self.load_data_json(archivo)
        persona = {
            'id' : nuevo_id,
            'nombre' : nombre,
            'edad' : edad
        }
        data.append(persona)
        with open(archivo, 'w') as file:
            json.dump(data, file, indent=4)
            
    def modificar_datos(self, archivo, id_actualizar, nombre= None, edad = None):
        data = self.load_data_json(archivo)
        for dato in data:
            if dato['id'] == int(id_actualizar):
                if nombre is not None:
                    dato['nombre'] = nombre
                    self.sobreescribir_archivo_json(archivo, data)
                    return f"Nombre Modificado a {nombre} en JSON"
                if edad is not None:
                    dato['edad'] = edad
                    self.sobreescribir_archivo_json(archivo, data)
                    return f"Edad Modificada a {edad} en JSON"
            break
                

    def sobreescribir_archivo_json(self, archivo, data):
        with open(archivo, 'w') as file:
            json.dump(data, file, indent=4)
    
    def incrementar_id(self, archivo):
        data = self.load_data_json(archivo)
        
        if len(data) < 1:
            return 1
        
        ultimo_id = int(data[-1]['id'])
        return ultimo_id+1
            
    def load_data_json(self, archivo) -> list[dict]:
        with open(archivo, 'r') as file:
            return list(json.load(file))

