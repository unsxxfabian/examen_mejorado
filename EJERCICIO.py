#EJERCICIO 1

#EXAMEN
import numpy as np
import matplotlib.pyplot as pl
x=[50,38,28,8,8,16,5,2]
y=[134844,55526,5523,4067,611,4459,2195,1225]


print(x)
n=len(x)
print("tamaño= ",n)
print(y)

x=np.array(x)
y=np.array(y)
print(x)
print(y)
sumax=sum(x)
print("sumax= ",sumax)
sumay=sum(y)
print("sumay= ",sumay)
promx=sumax/n
print("promx= ",promx)
promy=sumay/n
print("promy= ",promy)
sumax2=sum(x*x)
print("sumax^2",sumax2)

sumaxy=sum(x*y)
print("sumaxy= ",sumaxy)
b=(sumax*sumay-n*sumaxy)/(sumax**2-n*sumax2)
a=promy-b*promx
print("b= ",b," a= ",a)
pl.plot(x,y,'o',label='Datos')
pl.plot(x,a+b*x,label='Ajuste')

pl.xlabel('x')
pl.ylabel('y')
 vf
pl.grid()
pl.legend()
pl.show()