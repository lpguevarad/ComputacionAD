import matplotlib.pyplot as plt
import numpy as np

archivo1=open("DatosMarzo.txt","r")
archivo2=open("GRS_vs_EQ.txt","r")

x1=[]
y1=[]

for i in archivo1.readlines():
	line=i.split()
	#print(line)
	
	x1.append(float(line[0]))
	y1.append(float(line[1]))

x1=np.asarray(x1)
y1=np.asarray(y1)

	
x2=[]
y2=[]

for i in archivo2.readlines():
	line=i.split()
	#print(line)
	
	x2.append(float(line[0]))
	y2.append(float(line[1]))
	
x2=np.asarray(x2)
y2=np.asarray(y2)

plt.plot(x1,y1,linestyle="none",marker=".",color="olive",markersize=10,label="$Datos$ $Marzo$")
plt.plot(x2,y2,linestyle="none",marker=".",color="black",markersize=1,label="$Datos$ $Anuales$")

plt.xlabel("$Deslizamientos$ $glaciares$")
plt.ylabel("$Sismos$ $catastroficos$")

plt.legend(loc="best")
plt.show()

plt.savefig("PlotTolima.pdf")

