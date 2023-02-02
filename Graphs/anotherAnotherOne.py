import networkx as nx
import matplotlib.pyplot as plt
from collections import deque as dq

G = nx.Graph()
q = dq()


class Node:
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.edges = []

    def addEdge(self, edge):
        self.edges.append(edge)


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def addNode(self, node):
        self.nodes.append(node)


nodes = int(input())
# nodes = 5
nodesList = list(range(nodes))
print(nodesList)

for i in range(nodes):
    G.add_node(i)

edges = int(input())
# edges = 6
edgesList = []
for i in range(edges):
    edgesList.append(tuple(map(int, (input().split(' ')))))
    G.add_edge(*edgesList[-1])
print(edgesList)

for i in range(nodes):
    nodesList[i] = Node(i)

for i in edgesList:
    print(i)
    nodesList[i[0]].addEdge(i)
    nodesList[i[1]].addEdge(i)

for i in nodesList:
    print(i.value, i.edges)

print()
print(G.nodes)
print(G.edges)

for node in nodesList:
    print(f'node: {node.value}, edges: {node.edges}')

nx.draw(G, with_labels=True)
plt.show()
