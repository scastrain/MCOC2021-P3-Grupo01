import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

G = nx.Graph()

#fig1
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

#Agregando arcos (edges)
a = 2
G.add_edge(0,1, color='#6C4E09',weight=a)
G.add_edge(0,2, color='#7C7C7C',weight=a)
G.add_edge(0,6, color='#7C7C7C',weight=a)
G.add_edge(1,2, color='#6C4E09',weight=a)
G.add_edge(1,3, color='#00701A',weight=a)
G.add_edge(1,7, color='#6C4E09',weight=a)
G.add_edge(2,5, color='#6C4E09',weight=a)
G.add_edge(3,4, color='#00701A',weight=a)
G.add_edge(3,6, color='#6C4E09',weight=a)
G.add_edge(3,7, color='#00701A',weight=a)
G.add_edge(3,8, color='#6C4E09',weight=a)
G.add_edge(4,6, color='#7C7C7C',weight=a)
G.add_edge(4,8, color='#7C7C7C',weight=a)
G.add_edge(5,7, color='#7C7C7C',weight=a)
G.add_edge(7,9, color='#00701A',weight=a)
G.add_edge(8,9, color='#00701A',weight=a)

pos=nx.get_node_attributes(G,'pos')

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

#fig2
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

#Agregando arcos (edges)
a = 1
G.add_edge(0,1, color='r',weight=4) #rm
G.add_edge(0,2, color='#7C7C7C',weight=a)
G.add_edge(0,6, color='#7C7C7C',weight=a)
G.add_edge(1,2, color='#7C7C7C',weight=a)
G.add_edge(1,3, color='#7C7C7C',weight=a)
G.add_edge(1,7, color='r',weight=4) #rm
G.add_edge(2,5, color='#7C7C7C',weight=a)
G.add_edge(3,4, color='#7C7C7C',weight=a)
G.add_edge(3,6, color='#7C7C7C',weight=a)
G.add_edge(3,7, color='#7C7C7C',weight=a)
G.add_edge(3,8, color='#7C7C7C',weight=a)
G.add_edge(4,6, color='#7C7C7C',weight=a)
G.add_edge(4,8, color='#7C7C7C',weight=a)
G.add_edge(5,7, color='#7C7C7C',weight=a)
G.add_edge(7,9, color='r',weight=4) #rm
G.add_edge(8,9, color='#7C7C7C',weight=a)

pos=nx.get_node_attributes(G,'pos')

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
plt.title("Tiempo par 0-9: 0,27 HORAS")
plt.show()

#fig3
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

#Agregando arcos (edges)
a = 2
G.add_edge(0,1, color='#7C7C7C',weight=a)
G.add_edge(0,2, color='#7C7C7C',weight=a)
G.add_edge(0,6, color='#7C7C7C',weight=a)
G.add_edge(1,2, color='#7C7C7C',weight=a)
G.add_edge(1,3, color='#7C7C7C',weight=a)
G.add_edge(1,7, color='#7C7C7C',weight=a)
G.add_edge(2,5, color='#7C7C7C',weight=a)
G.add_edge(3,4, color='r',weight=4) #rm
G.add_edge(3,6, color='#7C7C7C',weight=a)
G.add_edge(3,7, color='r',weight=4) #rm
G.add_edge(3,8, color='#7C7C7C',weight=a)
G.add_edge(4,6, color='#7C7C7C',weight=a)
G.add_edge(4,8, color='#7C7C7C',weight=a)
G.add_edge(5,7, color='r',weight=4) #rm
G.add_edge(7,9, color='#7C7C7C',weight=a)
G.add_edge(8,9, color='#7C7C7C',weight=a)

pos=nx.get_node_attributes(G,'pos')

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
plt.title("Tiempo par 4-5: 0,19 HORAS")
plt.show()

#fig4
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

#Agregando arcos (edges)
a = 2
G.add_edge(0,1, color='#7C7C7C',weight=a)
G.add_edge(0,2, color='#7C7C7C',weight=a)
G.add_edge(0,6, color='r',weight=4) #rm
G.add_edge(1,2, color='#7C7C7C',weight=a)
G.add_edge(1,3, color='#7C7C7C',weight=a)
G.add_edge(1,7, color='#7C7C7C',weight=a)
G.add_edge(2,5, color='#7C7C7C',weight=a)
G.add_edge(3,4, color='#7C7C7C',weight=a)
G.add_edge(3,6, color='#7C7C7C',weight=a)
G.add_edge(3,7, color='#7C7C7C',weight=a)
G.add_edge(3,8, color='#7C7C7C',weight=a)
G.add_edge(4,6, color='r',weight=4) #rm
G.add_edge(4,8, color='#7C7C7C',weight=a)
G.add_edge(5,7, color='#7C7C7C',weight=a)
G.add_edge(7,9, color='#7C7C7C',weight=a)
G.add_edge(8,9, color='#7C7C7C',weight=a)

pos=nx.get_node_attributes(G,'pos')

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
plt.title("Tiempo par 0-4: 0,08 HORAS")
plt.show()