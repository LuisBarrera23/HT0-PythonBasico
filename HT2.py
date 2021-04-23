#Luis Angel Barrera Velásquez 
#Carnet: 202010223

#Ejercicio 1
def comparar(contraseña):
    contraseña2=str(input("¿Cúal fue la contraseña que ingreso anteriormente?").lower())
    if contraseña==contraseña2:
        print("La contraseña es correcta")
    else:
        print("No ha ingresado la misma contraseña")


contraseña1=str(input("Introduzca la contraseña que desea guardar").lower())
comparar(contraseña1)

#Ejercicio 2
def asigargrupo(nombre,genero):
    if (nombre[0].upper() in "ABCDEFGHIJKL") and genero=='F':
        print("Perteneces al grupo A")
    elif (nombre[0].upper() in "ÑOPQRSTUVWXYZ") and genero=='M':
        print("Perteneces al grupo A")
    elif (nombre[0].upper() in "MNÑOPQRSTUVWXYZ") and genero=='F':
        print("Perteneces al grupo B")
    elif (nombre[0].upper() in "ABCDEFGHIJKLMN") and genero=='M':
        print("Perteneces al grupo B")

nombre=str(input("Por favor ingresa tu nombre "))
genero=''
while not (genero=='M' or genero=='F'):
    genero=str(input("Ingresa tu genero: M para masculino y F para femenino").upper())

asigargrupo(nombre,genero)

# prueba