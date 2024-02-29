import os
import sys
import csv
import json

from tabulate import tabulate

products_file = "productos.csv"

# Este es el layout de los menús, imprime el titulo y el menu
def menus_layout(title:str,menu:list):
  print(title)
  print(tabulate(menu, tablefmt="grid"))

# Revisa el sistema operativo en el que está trabajando y borra la pantalla
def clear_screen():
  if sys.platform == "linux" or sys.platform == "darwin":
    os.system("clear")
  else:
    os.system("cls")

#crea un archivo json de people
people={

  'id': '',
  'Name': '',
  'Email': '',
  'Phone': {
    'Movil':'',
    'House':'',
    'Personal':'', 
    'Oficina':'',  
    },
}

def json_people(people):
  with open('data/people.json',"w") as pe:
    json.dump(people,pe, indent=4)

#crea un archivo json de zonas
zone={
  'NoZona': '',
  'NombreZona': '',
  'TotalCap': 35,
}

def json_zone(zone):
    with open('data/zone.json',"w") as zo:
        json.dump(zone,zo, indent=4)

#crea un archivo json de activos
active={
  'CodTransaccion': '',
  'NoFormulario': '',
  'CodCampus': '',
  'Marca': '',
  'Categoria': '',
  'Tipo': '',
  'ValorUnitario': '',
  'proveedor': '',
  'NoSerial': '',
  'EmpresaResponsable': '',
  'Estado': '',
  'Historial':{
    'Nrold': '',
    'Fecha': '',
    'TipoMovimiento': '',
    'IdRespMov': '',
  }
}

def json_active(active):
    with open('data/activo.json',"w") as ac:
        json.dump(active,ac, indent=4)


