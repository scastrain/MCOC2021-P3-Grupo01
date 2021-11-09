import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from math import dist

G = nx.Graph()

#Agregando nodos (nodes)
G.add_node(0, pos=[1,2])    #nombre puede ser cualquier cosa...
G.add_node(1, pos=[4,3])    #nombre puede ser cualquier cosa...
G.add_node(2, pos=[1,6])
G.add_node(3, pos=[7,3])
G.add_node(4, pos=[10,1])
G.add_node(5, pos=[0,10])
G.add_node(6, pos=[4,0])
G.add_node(7, pos=[5,8])
G.add_node(8, pos=[9,7])
G.add_node(9, pos=[8,10])

pos=nx.get_node_attributes(G,"pos")

#Tipos de calles y limites de velocidad
cafe=40
gris=120
verde=60
		

cost=[]
#Distancias y costos
posiciones=((pos[0],pos[1],cafe),
			(pos[0],pos[2],gris), 
			(pos[0],pos[6],gris), 
			(pos[1],pos[2],cafe), 
			(pos[1],pos[3],verde),
			(pos[1],pos[7],cafe),
			(pos[2],pos[5],cafe),
			(pos[3],pos[4],verde), 
			(pos[3],pos[6],cafe),
			(pos[3],pos[7],verde), 
			(pos[3],pos[8],cafe),
			(pos[4],pos[6],gris),
			(pos[4],pos[8],gris), 
			(pos[5],pos[7],gris),
			(pos[7],pos[9],verde), 
			(pos[8],pos[9],verde)
			)


for i in posiciones:
	a=i[0]
	b=i[1]
	vel=i[2]
	distancia=dist(a,b)
	#print(distancia)
	costo=distancia/vel
	cost.append(costo)


#Agregando Arcos con sus respectivos costos
a = 2
G.add_edge(0,1, color='#6C4E09',weight=a, costo=cost[0]) #0-1 cost[0]
G.add_edge(0,2, color='#7C7C7C',weight=a, costo=cost[1]) #0-2  .
G.add_edge(0,6, color='#7C7C7C',weight=a, costo=cost[2]) #0-6  .
G.add_edge(1,2, color='#6C4E09',weight=a, costo=cost[3]) #1-2  .
G.add_edge(1,3, color='#00701A',weight=a, costo=cost[4]) #1-3  .
G.add_edge(1,7, color='#6C4E09',weight=a, costo=cost[5]) #1-7  .
G.add_edge(2,5, color='#6C4E09',weight=a, costo=cost[6]) #2-5  .
G.add_edge(3,4, color='#00701A',weight=a, costo=cost[7]) #3-4  .
G.add_edge(3,6, color='#6C4E09',weight=a, costo=cost[8]) #3-6  . 
G.add_edge(3,7, color='#00701A',weight=a, costo=cost[9]) #3-7  .
G.add_edge(3,8, color='#6C4E09',weight=a, costo=cost[10]) #3-8  . 
G.add_edge(4,6, color='#7C7C7C',weight=a, costo=cost[11]) #4-6  . 
G.add_edge(4,8, color='#7C7C7C',weight=a, costo=cost[12]) #4-8  .
G.add_edge(5,7, color='#7C7C7C',weight=a, costo=cost[13]) #5-7  .
G.add_edge(7,9, color='#00701A',weight=a, costo=cost[14]) #7-9  .
G.add_edge(8,9, color='#00701A',weight=a, costo=cost[15]) #8-9  cost[15]



colors = nx.get_edge_attributes(G,'color').values()
weights = nx.get_edge_attributes(G,'weight').values()

fig, ax = plt.subplots()
ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

nx.draw(G, pos, edge_color=colors, width=list(weights), with_labels=True)
limits=plt.axis('on') # turns on axis
ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)


plt.xticks(np.arange(0.0,11.0,1.0))
plt.yticks(np.arange(0.0,11.0,1.0))
plt.grid(True, lw = 0.4)
plt.xlabel("X (km)")
plt.ylabel("Y (km)")
plt.show()


rutas1 = nx.all_simple_paths(G, source = 0, target = 9)
rutas2 = nx.all_simple_paths(G, source = 4, target = 5)
rutas3 = nx.all_simple_paths(G, source = 0, target = 4)

viajes = [rutas1, rutas2, rutas3]
n_v = 0

for viaje in viajes:

	first = 100
	n_v += 1
	sum_costo = 0
	costos_totales = []
	ruta_final = []

	for ruta in viaje:
		
		costo_ruta = 0.
		Nparadas = len(ruta)

		for i in range(Nparadas-1):

			parada_i = ruta[i]
			parada_f = ruta[i+1]

			costo_tramo_i = G.edges[parada_i, parada_f]["costo"]
			costo_ruta += costo_tramo_i
		costos_totales.append(costo_ruta)

		if first > costo_ruta:
			ruta_final = ruta

		first = min(costos_totales)


	print(f"el costo mínimo del viaje {n_v} es = {first} de la ruta {ruta_final} ")

	G.add_edge(0,1, color='#7C7C7C',weight=a) 
	G.add_edge(0,2, color='#7C7C7C',weight=a)
	G.add_edge(0,6, color='#7C7C7C',weight=a)
	G.add_edge(1,2, color='#7C7C7C',weight=a)
	G.add_edge(1,3, color='#7C7C7C',weight=a)
	G.add_edge(1,7, color='#7C7C7C',weight=a) 
	G.add_edge(2,5, color='#7C7C7C',weight=a)
	G.add_edge(3,4, color='#7C7C7C',weight=a)
	G.add_edge(3,6, color='#7C7C7C',weight=a)
	G.add_edge(3,7, color='#7C7C7C',weight=a)
	G.add_edge(3,8, color='#7C7C7C',weight=a)
	G.add_edge(4,6, color='#7C7C7C',weight=a)
	G.add_edge(4,8, color='#7C7C7C',weight=a)
	G.add_edge(5,7, color='#7C7C7C',weight=a)
	G.add_edge(7,9, color='#7C7C7C',weight=a)
	G.add_edge(8,9, color='#7C7C7C',weight=a)

	c = len(ruta_final)
	for j in range(c-1):
		
		G.add_edge(ruta_final[j], ruta_final[j+1], color = 'r', weight = 4)


	colors = nx.get_edge_attributes(G,'color').values()
	weights = nx.get_edge_attributes(G,'weight').values()

	fig, ax = plt.subplots()
	ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
	ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

	nx.draw(G, pos, edge_color=colors, width=list(weights), with_labels=True)
	limits=plt.axis('on') # turns on axis
	ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)

	plt.title(f"Viaje {n_v}")
	plt.xticks(np.arange(0.0,11.0,1.0))
	plt.yticks(np.arange(0.0,11.0,1.0))
	plt.grid(True, lw = 0.4)
	plt.xlabel("X (km)")
	plt.ylabel("Y (km)")
	plt.show()





