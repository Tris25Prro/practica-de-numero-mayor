n=[[],[],[],[],[],[],[],[],[],[]]
def numeros():
    
    print("presiona enter para poder agregar mas numeros \n")
    print ("Agrega 10 numeros " )
    for tri in range(0,10):
        m= int(input("agrega un numero aleatorio: "))
        n[tri].append(m)
numeros()
print("\n",n, "el mayor es: ", max(n), "\n")


