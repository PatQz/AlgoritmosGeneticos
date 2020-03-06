import random
import math
#clase indivio: estructura del individuo, incluye una cadena x & una cadena y
class Individuo:
    def __init__(self):
        self.x=[]
        self.y=[]

#Generar Individuo genera dos cadenas de 1 y 0 al azar y crea un nuevo individuo 
#dando las cadenas al azar a su x & y
def generarIndividuo(tamanoBits):
    a,b = [],[]
    
    for i in range(0,tamanoBits):
      r=random.randint(0,1)
      a.append(r)
      
    for i in range(0,tamanoBits):
      r1=random.randint(0,1)
      b.append(r1)
      
    ind=Individuo()
    ind.x=a
    ind.y=b
    return ind

#Binario a decimal convierte una cadena binaria a un numero decimal
def bad(a,tamanoBits,rango): #binario a decimal
    aux,aux2,aux3,auxc=0.0,0.0,0.0,0.0
    c=[]
      
    for i in range(0,tamanoBits):
        c.append(1)
    #se toma el valor maximo de un numero binario en el tamano de bits indicado
    for i in range(0,tamanoBits-1):
        auxc += c[i]*(2**i)
    #se obtiene el valor de la cadena binaria a
    j=tamanoBits-1
    for i in range(0,tamanoBits-1):
        aux += a[j]*(2**i)
        j-=1
	#se divide el tamano del rango de el maximo valor y el rango actual desde 
	#su contraparte negativa hasta el positivo
    aux2=(auxc*2)/(rango*2)
	#se divide el numero actual entre el valor anteriormente obtenido
    aux3= aux/aux2
    return aux3
#genera una poblacion dependiendo de un valor indicado
def generarPoblacion(n,tamanoBits):
    a=[]
    for i in range(n):
        a.append(generarIndividuo(tamanoBits))
    return a
#funciones de dejoung
def fitness(a,b,tamanoBits,rango,funcion):
	x=bad(a,tamanoBits,rango)
	y=bad(b,tamanoBits,rango)
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
def seleccionPoblacion(poblacion,tamanoBits,rango,n):
	newPoblacion = range(len(poblacion))
	#TORNEOS
	for i in range(len(poblacion)):
		r1,r2 = random.choice(range(len(poblacion))),random.choice(range((len(poblacion))))       
		if fitness(poblacion[r1].x,poblacion[r1].y,tamanoBits,rango,n) < fitness(poblacion[r2].x,poblacion[r2].y,tamanoBits,rango,n):
		  newPoblacion[i] = (poblacion[r1])
		else:
	  	  newPoblacion[i] = (poblacion[r2])
	return newPoblacion
#Se obtienen dos individuos al azar de la poblacion y 
#dependiendo de si un numero al azar flotante es menor que el valor
#asignado de la probabilidad de cruzamiento se cruzan o no los individuos
def cruzarPoblacion(poblacion):
	C = 0.85
	for i in range(len(poblacion)-1):
	    azar1=random.randint(0,len(poblacion)-1)
	    azar2=random.randint(0,len(poblacion)-1)
	    if C > random.random():
	    	poblacion[azar1], poblacion[azar2] = cruzamiento(poblacion[azar1], poblacion[azar2])

def cruzamiento(ind1,ind2):
    #cambia la mitad de cada x & y del individuo
    #se cruza con todo y bit de signo
	ax,bx,cx,dx=[],[],[],[]
	ay,by,cy,dy=[],[],[],[]
	ax = ind1.x[:len(ind1.x)/2]
	bx = ind1.x[(len(ind1.x)/2):]
	cx = ind2.x[:len(ind2.x)/2]
	dx = ind2.x[(len(ind2.x)/2):]
	
	ay = ind1.y[:len(ind1.y)/2]
	by = ind1.y[(len(ind1.y)/2):]
	cy = ind2.y[:len(ind2.y)/2]
	dy = ind2.y[(len(ind2.y)/2):]
	#se juntan las partes obtenidas
	newi1,newi2=Individuo(), Individuo()
	newi1.x = ax+dx
	newi2.x = cx+bx
	newi1.y = ay+dy
	newi2.y = cy+by

	return newi1,newi2
#Se obtienen un individuo al azar de la poblacion y 
#dependiendo de si un numero al azar flotante es menor que el valor
#asignado de la probabilidad de mutacion se muta o no
def mutarPoblacion(poblacion):
    proBM=0.1
    for i in range(len(poblacion)):
         if(random.random() < proBM):
            azar=random.randint(0,len(poblacion)-1)
            poblacion[azar] = mutacion(poblacion[azar])
#se muta un elemento al azar de x & y de un individuo 
def mutacion(ind):
    z=random.randint(0,1)
    newInd = Individuo()
    a,b=[],[]
    a=ind.x
    b=ind.y
    azar=random.randint(0,len(ind.x)-1)
    a[azar] = random.randint(0,1)
    b[azar] = random.randint(0,1)
    newInd.x= a
    newInd.y= b
    return newInd
    
def imprimir(Poblacion,tamBits,rango):
    for j in range(len(Poblacion)):
        print bad(Poblacion[j].x,tamBits,rango),"   \t",bad(Poblacion[j].y,tamBits,rango),"   \t",fitness(Poblacion[j].x,Poblacion[j].y,tamBits,rango,4)
    
#/////////////////////////////////////////////////////////////////////#
#1)matyas -10 <= x,y <=10 /f(0,0)=0
#2)easom	-100 <= x,y <=100 /f(pi,pi)=-1 
#3)goldenstein-price 	 -2 <= x,y <=2 /f(0,-1)=3
#4)Ackley's 	-2 <= x,y <=2 /f(0,0)=0
#5)levi	-10 <= x,y <=10 /f(1,1)=0
#6)Schaffer function N. 2	-100 <= x,y <=100 /f(0,0)=0
#7)Schaffer function N. 4	-100 <= x,y <=100 /f(0,1.25313)=0.292579

tamanoBits=20 #4 bits + bit de signo
rango=2

p=generarPoblacion(10,tamanoBits)

print "----------------------------"
for i in range(1000):
   p = seleccionPoblacion(p,tamanoBits,rango,4)
   cruzarPoblacion(p)
   mutarPoblacion(p)
print "----------------------------"
imprimir(p,tamanoBits,rango)