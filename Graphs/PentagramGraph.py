import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add some vertices
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
# G.add_node(6)

# Add some edges
# G.add_edge(1, 1)
G.add_edge(1, 2)
# G.add_edge(2, 1)
G.add_edge(1, 3)
G.add_edge(1, 4)
G.add_edge(2, 3)
G.add_edge(2, 4)
G.add_edge(2, 5)
G.add_edge(3, 4)
G.add_edge(3, 5)
G.add_edge(4, 5)
G.add_edge(5, 1)

print(G.nodes)
print(G.edges)
# nx.draw(G, with_labels=True, arrows=True)
nx.draw(G, with_labels=True)

plt.show()

