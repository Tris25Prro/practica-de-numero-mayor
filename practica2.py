n=[[],[],[],[],[],[],[],[],[],[]]
def numeros():
    print ("Agrega 10 numeros ", "presiona enter para poder agregar mas numeros")
    for tri in range(0,10):
        m= int(input("agrega un numero aleatorio: "))
        n[tri].append(m)
numeros()
print("\n",n, "el mayor es: ", max(n), "\n")

