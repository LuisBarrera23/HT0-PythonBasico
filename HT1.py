#Luis Angel Barrera Velásquez 
#Carnet: 202010223

#Ejercicio 1

print("imprimiendo un arbol de asteriscos")
nivel=int(input("introduce el numero de niveles que quieres que tenga el arbol"))

for i in range(nivel+1):
    print (i*"*")

#Ejercicio 2

print("Verificacion de un numero primo")
numero=int(input("ingrese el numero que quiera verificar: "))

verificador=0

for i in range(1,numero+1):
    if numero%i==0:
        verificador+=1
        

if verificador==2:
    print("El numero es primo")
else:
    print("El numero no es primo")
