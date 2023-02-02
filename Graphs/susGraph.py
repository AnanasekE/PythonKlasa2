import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
nodes = int(input())

for i in range(nodes):
    G.add_node(i)

for i in range(nodes//2):
    for j in range(i*2, i*2+2):
        G.add_edge(i, j+1)


print(G.nodes)
print(G.edges)
nx.draw(G, with_labels=True)
plt.show()
