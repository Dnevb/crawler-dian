# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# CHROMEDRIVER_PATH = './chromedriver'
# WINDOW_SIZE = "1920,1080"

# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
# chrome_options.add_argument('--no-sandbox')
# driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
#                           chrome_options=chrome_options
#                          )
# driver.get("https://www.google.com")
# print(driver.title)
# driver.close()

import json
from io import open

def menu():
    while True:
        print("-"*20)
        print("1. Adicionar")
        print("2. Buscar")
        print("3. Eliminar")
        print("4. Listar")
        print("5. Salir")
        print("-"*20)

        opcion = int(input("Digite la opcion: "))

        if opcion == 1:
            adicionar()
        elif opcion == 2:
            ced = input("Cedula a buscar? ")
            buscar(ced)
        elif opcion == 3:
            ced = input("Cedula a elminar? ")
            eliminar(ced)
        elif opcion == 4:
            listar()
        elif opcion == 5:
            break

def adicionar():
    with open('agenda.json','r+') as f:
        lista = json.load(f)
    num = int(input("Cuantos registros desea ingresar? "))

    for i in range(num):
        agenda = {}
        nombre = input("nombre: ")
        cedula = input("cedula: ")
        agenda['Nombre'] = nombre
        agenda['Cedula'] = cedula
        lista.append(agenda)

    with open('agenda.json','w') as file:
        json.dump(lista, file)
        print("Archivo importado")

def listar():
    with open('agenda.json','r') as f:
        agenda1 = json.load(f)

        for i in agenda1:
            print("Nombre: {0} Cédula: {1}".format(i["Nombre"],i["Cedula"])) 

def buscar(ced):
    
    with open('agenda.json','r') as f:
        agenda1 = json.load(f)

        for i in agenda1:
            if i["Cedula"] == ced:
                print("Nombre: {0} Cédula: {1}".format(i["Nombre"],i["Cedula"]))
                return
            
        print("La cédula no existe")    


def eliminar(ced):
    with open('agenda.json','r+') as f:
        agenda1 = json.load(f)

    for i,v in enumerate(agenda1):
        if v["Cedula"] == ced:
            agenda1.pop(i)
            print("Elemento eliminado")
            with open('agenda.json','w') as f:
                json.dump(agenda1, f)
            return
            
        print("La cédula no existe")  
    

menu()