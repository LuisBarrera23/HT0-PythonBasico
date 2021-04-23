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