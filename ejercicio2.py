import numpy as np
import matplotlib.pyplot as pl

from sklearn.cluster import KMeans
#from sklearn import Metrics


v1=[50,38,28,8,8,16,5,2]
v2=[134844,55526,5523,4067,611,4459,2195,1225]
print(v1)
print(v2)
x1=np.array(v1)
x2=np.array(v2)
x=np.array(list(zip(x1,x2))).reshape(len(x1),2)
pl.plot(x1,x2,'o',label="D")

pl.xlabel('x')
pl.ylabel('y')
pl.grid()
pl.legend()
pl.show()

k=3 
modelo_kmeans=KMeans(n_clusters=k).fit(x)


for i,l in enumerate(modelo_kmeans.labels_):
    print("(x1,x2)->:clase")
    print("({0},{1})->:{2}".format(x1[i],x2[i],l))
    

#calculando los centroides
print("centroides: ")
centroides=modelo_kmeans.cluster_centers_
print(centroides)
c1=centroides[0]
c2=centroides[1]
c3=centroides[2]
print("los centroides:")
print(c1)
print("los centroidesss: ")
cx1=c1[0]
print(cx1)
#para graficar
cx=[c1[0],c2[0],c3[0]]
cy=[c1[1],c2[1],c3[1]]


pl.plot(x1,x2,'o',label="puntos")
pl.plot(cx,cy,'o',label="centroides")
#pl.plot(c1[0],c1[1],'o',label="centroides")
#pl.plot(c2[0],c2[1],'o')
#pl.plot(c3[0],c3[1],'o')
pl.xlabel('x')
pl.ylabel('y')
pl.grid()
pl.legend()
pl.show()
print("-------------------------------------------")
pl.plot(x1,x2,'o',label="puntos")
pl.plot(c1[0],c1[1],'o',label="c1")
pl.plot(c2[0],c2[1],'o',label="c2")
pl.plot(c3[0],c3[1],'o',label="c3")
pl.xlabel('x')
pl.ylabel('y')
pl.grid()
pl.legend()
pl.show()