import csv

def read_csv_users():
    with open("usuarios.csv", "r") as file:
        data = csv.DictReader(file)
        return list(data)