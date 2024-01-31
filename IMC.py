name = input("Ingresa tu nombre")
if name == "":
    print("Campo invalido")
lastname = input("Ingresa tu apellido paterno")
if lastname == "":
    print("Campo invalido")
lastname2 = input("Ingresa tu apellido materno")
if lastname2 == "":
    print("Campo invalido")
age = input("Ingresa tu edad") 
if age == "":
    print("Campo invalido")
weight = int(input("Ingresa tu peso"))
if weight == "":
    print("Campo invalido")
height = int(input("Ingresa tu altura"))
if height == "":
    print("Campo invalido")

try:
    imc = weight / height **2
except:
    print ( "Hola su IMC es " + str(imc))
