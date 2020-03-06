import random
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#genera un individuo con numeros al azar entre el 0 y 7
def generarIndividuo():
    queen = range(8)
    random.shuffle(queen)
    return queen 
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#genera una poblacion de n individuos
def generarPoblacion(n):
	poblacion = []
	for i in range(n):
		poblacion.append(generarIndividuo())
	return poblacion
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#calcula el numero de ataques de una reina
def ataques(queen):
    ataques = 0
    for i in range(len(queen)):
        for j in range(len(queen)):
            if i!=j: 
                if queen[i] == queen[j]: ataques+=1
                if queen[i]-queen[j] == i-j: ataques+=1
    return ataques
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#seleccion de la poblacion con torneos: se toman dos reinas al azar de la poblacion y
#dependiendo de el numero de ataques de cada reina, se toma la de menor numero de 
#ataques y se agrega a una nueva poblacion
def seleccionarPoblacion(poblacion):
    newPoblacion = range(len(poblacion))
    for i in range (len(poblacion)): 
        r1 = random.choice(poblacion)
        r2 = random.choice(poblacion)
        if ataques(r1) < ataques(r2):
           newPoblacion[i]=r1
        else:
           newPoblacion[i]=r2
    return newPoblacion
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#el cruzamiento se realiza tomando la mitad de cada reina 
#e intercambiando su segunda mitad con el otro individuo
def cruzarIndividuos(reina1,reina2):
    n = (len(reina1)/2) - 1
    p,q = [],[]
    for i in range(n): 
        p.append(reina1[i]) 
        q.append(reina2[i])
    
    for i in range(n,len(reina2)): 
        p.append(reina2[i])
        q.append(reina1[i])
    return p,q
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#Se obtienen dos individuos al azar de la poblacion y 
#dependiendo de si un numero al azar flotante es menor que el valor
#asignado de la probabilidad de cruzamiento se cruzan o no los individuos
def cruzarPoblacion(poblacion):
    C = 0.85
    for i in range(len(poblacion)):
        azar1=random.randint(0,len(poblacion)-1)
        azar2=random.randint(0,len(poblacion)-1)
        if C > random.random():
            poblacion[azar1], poblacion[azar2] = cruzarIndividuos(poblacion[azar1], poblacion[azar2])      
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#para mutar se elije una posicion al azar del individuo y se cambia por un uno o por un cero generado aleatoriamente
def mutarIndividuo(reina):
    r = random.randint(0,len(reina)-1)
    p = random.randint(0,len(reina)-1)
    reina[r] = p
    return reina
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#Se obtienen un individuo al azar de la poblacion y 
#dependiendo de si un numero al azar flotante es menor que el valor
#asignado de la probabilidad de mutacion se muta o no
def mutarPoblacion(poblacion):
    proBM=0.1
    for i in range(len(poblacion)):
         if(random.random() < proBM):
            azar=random.randint(0,len(poblacion)-1)
            poblacion[azar] = mutarIndividuo(poblacion[azar])
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def imprimir(poblacion):
    for i in range(len(poblacion)):
        print poblacion[i], ataques(poblacion[i])
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def imprimirMejor(poblacion):
    for i in range(len(poblacion)-1):
        print poblacion[i], ataques(poblacion[i])
        if(poblacion[i] == poblacion[i+1]): break
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def menorAtaques(poblacion):
    aux = []
    for i in range(len(poblacion)):
        if(ataques(poblacion[i]) == 0):
            aux.append(poblacion[i])
    return aux
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
p,q,r,t,aux = [],[],[],[],[]
p = generarPoblacion(100)
#imprimir(p)
 	
for i in range(50):
   p = seleccionarPoblacion(p)
   cruzarPoblacion(p)
   mutarPoblacion(p)

imprimirMejor(menorAtaques(p))