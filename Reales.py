# -*- coding: utf-8 -*-
import random
import math
class Individuo:
    def __init__(self):
        self.x=0.0
        self.y=0.0    

    def setx(self,x):
        self.x=x
    
    def sety(self,y):
        self.y=y
	
def generarIndividuo():
    r1,r2= random.uniform(-10, 10), random.uniform(-10, 10)
    ind = Individuo()
    if r1 > r2:
        r1, r2 = r2, r1
    ind.setx(r1)
    ind.sety(r2)
    return ind
#genera una poblacion dependiendo de un valor indicado	
def generarPoblacion(n):
    a=[]
    for i in range(n):
        a.append(generarIndividuo())
    return a
	
#funciones de dejoung
def fitness(a,b,funcion):
	x=a
	y=b
	r=0.0
	if funcion == 1: #matyas
		r= ((0.26*(x*x + y*y))-(0.48*(x*y)))
	elif funcion == 2: #easom
		r = - math.cos(x) * math.cos(y) * math.exp(- (((x-math.pi)*(x-math.pi)) +  ((y-math.pi)*(y-math.pi))))
	elif funcion == 3: #goldenstein-price
		aux1=(1 + ((x+y+1)**2)*(19-(14*x)+(3*(x**2))-(14*y)+(6*(x*y))+(3*(y**2))))
		aux2=(30+((2*x - 3*y)**2)*(18-(32*x)+(12*(x**2))+(48*y)-(36*(x*y))+(27*(y**2))))
		r=aux1*aux2
	elif funcion == 4: #Ackley's 
		r = (-20.0*math.exp(-0.2*math.sqrt(0.5*(x**2 + y**2))) - math.exp(math.cos(2.0*math.pi*x) + math.cos(2.0*math.pi*y)) + 20 + math.e)
	elif funcion == 5: #levi
		aux1 = math.sin(3 * math.pi * x)**2
		aux2 = 1+math.sin(3 * math.pi * y)**2
		aux3 = 1+math.sin(2 * math.pi * y)**2
		r = aux2 + ((x-1)**2)*aux2 + ((y-1)**2)*aux3
	elif funcion == 6: #Schaffer function N. 2
		aux1=(math.sin((x**2)-(y**2))**2)-0.5
		aux2=(1+0.001*((x**2)+(y**2)))**2
		r=0.5+(aux1/aux2)
	elif funcion == 7: #Schaffer function N. 4
		aux1=math.cos((math.sin((x**2)-(y**2))**2))**2-0.5
		aux2=(1+0.001*((x**2)+(y**2)))**2
		r=0.5+(aux1/aux2)
	else: 
		print "funcion no existe"
	return r
#Se utiliza la seleccion por torneos(MINIMIZACION), donde se compara el fitness de dos
#individuos al azar y se agrega a una nueva poblacion el menor de estos
def seleccionPoblacion(poblacion,n):
    newPoblacion = range(len(poblacion))
   
    #TORNEOS
    for i in range(len(poblacion)):
        r1,r2 = random.choice(range(len(poblacion))),random.choice(range((len(poblacion))))       
        if fitness(poblacion[r1].x,poblacion[r1].y,n) < fitness(poblacion[r2].x,poblacion[r2].y,n):
            newPoblacion[i] = (poblacion[r1])
        else:
            newPoblacion[i] = (poblacion[r2])
    return newPoblacion

#Se obtienen dos individuos al azar de la poblacion y 
#dependiendo de si un numero al azar flotante es menor que el valor
#asignado de la probabilidad de cruzamiento se cruzan o no los individuos
def cruzarPoblacion(poblacion,n):
    C = 0.85
    for i in range(len(poblacion)-1):
        azar1=random.randint(0,len(poblacion)-1)
        azar2=random.randint(0,len(poblacion)-1)
        if C > random.random():
            poblacion[azar1], poblacion[azar2] = cruzamiento(poblacion[azar1], poblacion[azar2],n)
#para el cruzamiento se soma en cuenta el mejor de los individuos dependiendo 
#de su fitness y se "mejora" el peor entre los dos individuos asignandole 
#un x & y generados al azar entre los dos individuos introducidos
def cruzamiento(ind1,ind2,n):
    if fitness(ind1.x,ind1.y,n) < fitness(ind2.x,ind2.y,n):
        chilo = ind1
        nochilo = ind2 #no chilo
    else: 
        chilo = ind2
        nochilo = ind1 #no chilo

    auxX=random.uniform(chilo.x,nochilo.x)
    auxY=random.uniform(chilo.y,nochilo.y)
    nochilo.x = auxX
    nochilo.y = auxY

    return chilo,nochilo
#Se obtienen un individuo al azar de la poblacion y 
#dependiendo de si un numero al azar flotante es menor que el valor
#asignado de la probabilidad de mutacion se muta o no
def mutarPoblacion(poblacion):
    proBM=0.1
    for i in range(len(poblacion)):
         if(random.random() < proBM):
            azar=random.randint(0,len(poblacion)-1)
            poblacion[azar] = mutacion(poblacion[azar])
#para la mutacion solo se genera un valor flotante entre 0 y 1 
#y se le suma al valor a mutar
def mutacion(ind):
    newind = Individuo()
    z=random.randint(0,1)
    aux = random.uniform(-1, 1)
    
    if(z==0):
        newind.x = ind.x + aux
    else:
        newind.y = ind.y + aux
    return newind   

def imprimir(Poblacion,n):
    for j in range(len(Poblacion)):
        print Poblacion[j].x,"   \t",Poblacion[j].y,"   \t",fitness(Poblacion[j].x,Poblacion[j].y,n)
#/////////////////////////////////////////////////////////////////////#
#1)matyas -10 <= x,y <=10 /f(0,0)=0
#2)easom	-100 <= x,y <=100 /f(pi,pi)=-1 
#3)goldenstein-price 	 -2 <= x,y <=2 /f(0,-1)=3
#4)Ackley's 	-2 <= x,y <=2 /f(0,0)=0
#5)levi	-10 <= x,y <=10 /f(1,1)=0
#6)Schaffer function N. 2	-100 <= x,y <=100 /f(0,0)=0
#7)Schaffer function N. 4	-100 <= x,y <=100 /f(0,1.25313)=0.292579

poblacion=generarPoblacion(100)
#imprimir(poblacion)

print "-----------------------------"
for i in range(1000):
   poblacion = seleccionPoblacion(poblacion,1) #el numero es el numero de funcion a probar
   cruzarPoblacion(poblacion,1)
   mutarPoblacion(poblacion)
print "-----------------------------"
imprimir(poblacion,1)