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

    def add_edge(self, edge):
        self.edges.append(edge)

    def __str__(self):
        return f'node: {self.value}, edges: {self.edges}'


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, node):
        self.nodes.append(node)

    def __str__(self):
        return f'nodes: {self.nodes}, edges: {self.edges}'


def create_nodes(nodes):
    nodes_list = [Node(i) for i in range(nodes)]
    G.add_nodes_from([i for i in range(nodes)])
    return nodes_list


def create_edges(edges, nodes_list):
    edges_list = []
    for i in range(edges):
        edge = tuple(map(int, input().split(' ')))
        edges_list.append(edge)
        nodes_list[edge[0]].add_edge(edge)
        nodes_list[edge[1]].add_edge(edge)
    return edges_list


try:
    nodes = int(input())
    edges = int(input())
    output = []

    print(f'nodes: {nodes}, edges: {edges}')

    nodes_list = create_nodes(nodes)
    edges_list = create_edges(edges, nodes_list)

    for edge in edges_list:
        G.add_edge(*edge)

    for node in nodes_list:
        print(node)
        q.append(node)
        # node.visited = True
    # while q:
    #     y = q.popleft()
    #     for edge in y.edges:
    #         if not nodes_list[edge[0]].visited:
    #             q.append(nodes_list[edge[0]])
    #             nodes_list[edge[0]].visited = True
    #         if not nodes_list[edge[1]].visited:
    #             q.append(nodes_list[edge[1]])
    #             nodes_list[edge[1]].visited = True
    #         print(f'edge: {edge}, q: {[i.value for i in q]}, z: {y.value}')
    #         output.append(y.value)
    # print(output)

    nx.draw(G, with_labels=True)
    plt.show()
except ValueError:
    print("Invalid input. Please enter a valid number.")
