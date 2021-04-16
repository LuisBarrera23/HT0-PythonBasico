import math

#variables a utilizar

print("Calculo de indice de masa corporal")
peso=float(input("introduce tu peso en kg"))
altura=float(input("introduce tu altura en metros"))
imc=round((peso/(altura**2)),2)
print("Tu indice de masa corporal es ",imc)