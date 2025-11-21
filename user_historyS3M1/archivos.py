import csv
import os
import tkinter as tk
from tkinter import filedialog

fieldnames = ['name','price','amount']
    
def save_csv(inventario, incluir_heads=True):
    if len(inventario):
        try:
            ruta = request_ruta("directory")
            file_exist = os.path.isfile(ruta + "/inventario.csv") # valida si el archivo existe
            with open(ruta + "/inventario.csv", 'a', newline='', encoding='utf-8') as archivo:
                writer = csv.DictWriter(archivo, fieldnames=fieldnames)
                if not file_exist: #si es True se añaden los encabezados, de lo contrario no se añaden
                    #Escribir encabezados
                    writer.writeheader()
                    
                
                #Escribir las filas
                writer.writerows(inventario)
                print("\033[32mInventario guardado en -->",ruta, "\033[0m")
        except Exception:
            print("Error al cargar información al archivo")
    else:
            print("\033[31mEl archivo no puede estar vacío\033[0m")

def load_csv(ruta = None):
    if ruta is None:
        ruta = request_ruta().name
    else:
         ruta = "inventario.csv"
    with open(ruta, 'r', encoding='utf-8', newline='') as archivo:
        lector = csv.DictReader(archivo)
        return list(lector)
     
    
def cargar_csv():
    if os.path.exists("inventario.csv"):
        opcion = input("Desea sobreescribir el archivo? S/n ").lower()
        if opcion == 's':
            print("Sobreescribir")
            overwrite_csv()
        elif opcion == 'n':
            print("agregar")
            no_overwrite()
        else: print(" opcion invalida")


def overwrite_csv():
    data = load_csv()
    with open("inventario.csv", 'w', newline='', encoding='utf-8') as archivo:
        writer = csv.DictWriter(archivo, fieldnames=fieldnames)
        #Escribir encabezados
        writer.writeheader()
        writer.writerows(data)

def no_overwrite():
    data = load_csv()
    with open("inventario.csv", 'a', newline='', encoding='utf-8') as archivo:
        writer = csv.DictWriter(archivo, fieldnames=fieldnames)
        writer.writerows(data)

                 
    
def request_ruta(type="file"):

    if type == "file":
        # Abrir el explorador de archivos
        ruta_carpeta = filedialog.askopenfile(title="Selecciona un archivo")        
        return ruta_carpeta 
    else:
        # Abrir el explorador de archivos
        ruta_carpeta = filedialog.askdirectory(title="Selecciona una carpeta")        
        return ruta_carpeta


def validate_exists(ruta):
    data = load_csv(ruta)