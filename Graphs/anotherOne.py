import networkx as nx
import matplotlib.pyplot as plt
from collections import deque as dq

G = nx.Graph()
q = dq()

nodes = int(input()) -1
# nodes = 5
for i in range(nodes):
    G.add_node(i)

edges = int(input())
# edges = 6
# edgesList = [(1, 2), (1, 3), (3, 4), (4, 0), (2, 3), (3, 0)]
edgesList = []

for i in range(edges):
    edgesList.append(tuple(map(lambda x: x-1, map(int, (input().split(' '))))))

print(edgesList)
for i in edgesList:
    G.add_edge(*i)
    q.append(i)
print()
print(q)

# for i in q:
#     G.nodes[i[0]]['visited'] = True
#     G.nodes[i[1]]['visited'] = True
#
#     for j in range(2):
#         if not G.nodes[i[0]]['visited']:
#             G.nodes[i[0]]['visited'] = True
#             q.append(i[0])

visitedEdges = []
visitedNodes = []
while q:
    edge = q.popleft()
    visitedEdges.append(edge)
    for node in edge:
        if node not in visitedNodes:
            visitedNodes.append(node)
            for edge in G.edges(node):
                if edge not in visitedEdges:
                    q.append(edge)
                    print('-----------------------')
                    print(f'visitedEdges: {visitedEdges}')
                    print(f'visitedNodes: {visitedNodes}')

nx.draw(G, with_labels=True)
plt.show()
