"""
Find Shortest Paths
"""

from math import inf
from typing import Optional
from graph_utils import *


class SPNode(Node):
    def __init__(self, label, links: List["SPLink"] = None, visited=False):
        super().__init__(label, links, visited)
        self.shortest: Optional[Link] = None
        self.distance = +inf


class SPLink(Link):
    def __init__(self, from_node: "SPNode", to_node: "SPNode", cost=0):
        super().__init__(from_node, to_node, cost)
        self.distance = +inf


def shortest_path(graph: Graph, node_idx=0):
    def remove_inside_links(links):
        remove = []
        for link in links:
            if link.to_node.distance < inf:
                remove.append(link)
        for link in remove:
            links.remove(link)

    def shortest_link(links):
        for link in links:
            link.distance = link.from_node.distance + link.cost
        return min(links, key=lambda link: link.distance)

    start_node: SPNode = graph.nodes[node_idx]
    start_node.distance = 0
    links: List[SPLink] = start_node.links[:]

    while links:
        min_link = shortest_link(links)
        # print(min_link)
        min_link.to_node.shortest = min_link
        min_link.to_node.distance = min_link.distance
        links.extend(min_link.to_node.links)
        remove_inside_links(links)

    for node in graph.nodes:
        print(node.label, node.distance, node.shortest)


def sp_test_graph():
    node_labels = [label for label in "ABCDEFGHIJKLMNOP"]
    nodes = [SPNode(label) for label in node_labels]
    node_neighbors = {
        "A": [("B", 5), ("E", 10), ("F", 12)],
        "B": [("C", 5), ("F", 11), ("A", 4)],
        "C": [("D", 7), ("G", 10)],
        "D": [("H", 11)],
        "E": [("F", 5), ("I", 9)],
        "F": [("G", 5), ("J", 11), ("K", 12)],
        "G": [("H", 6), ("K", 12), ("B", 4)],
        "H": [("L", 14), ("G", 5)],
        "I": [("J", 6), ("M", 10)],
        "J": [("K", 6), ("N", 12)],
        "K": [("L", 10), ("O", 15)],
        "L": [("P", 7)],
        "M": [("N", 7)],
        "N": [("O", 6)],
        "O": [("P", 9)],
        "P": [],
    }
    label2node = {node.label: node for node in nodes}
    links = []
    for node in nodes:
        for neighbor_tup in node_neighbors[node.label]:
            link = SPLink(node, label2node[neighbor_tup[0]], neighbor_tup[1])
            links.append(link)
            node.links.append(link)
    # print(nodes, links)
    return Graph(nodes, links)


g = sp_test_graph()
print(g)
shortest_path(g, 0)
