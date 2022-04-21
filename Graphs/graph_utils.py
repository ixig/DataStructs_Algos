"""
Helper Utilities for Creating Graphs
"""

from typing import List
from random import choice, random


class Node:
    def __init__(self, label, links: List["Link"] = None, visited=False):
        self.label = label
        self.links = links if links is not None else []
        self.visited = visited

    def __repr__(self):
        return str(self.label)

    def copy(self) -> 'Node':
        return Node(self.label)


class Link:
    def __init__(self, from_node: Node, to_node: Node, cost=0):
        self.from_node = from_node
        self.to_node = to_node
        self.cost = cost

    def __repr__(self):
        cost = f'{self.cost}' if isinstance(self.cost, int) else f'{self.cost:.3f}'
        return f"{self.from_node}->{self.to_node}/{cost}"

    def set_cmpl(self, link: 'Link'):
        self.cmpl = link

    def copy(self, from_node: Node, to_node: Node) -> 'Link':
        return Link(from_node, to_node, self.cost)


class Graph:
    def __init__(self, nodes: List[Node], links: List[Link], directed=True):
        self.nodes = nodes
        self.links = links
        self.directed = directed
        self.check()

    def __str__(self):
        s = ""
        for node in self.nodes:
            s += f"{node.label}: "
            for link in node.links:
                cost = f'{link.cost}' if isinstance(link.cost, int) else f'{link.cost:.3f}'
                s += f"{link.to_node}/{cost}, "
            s = s.rstrip(", ") + "\n"
        return s

    def check(self):
        if not self.directed:
            for link1 in self.links:
                assert link1.cmpl in self.links
                for link2 in self.links:
                    if link2.from_node is link1.to_node and link2.to_node is link1.from_node:
                        break
                else:
                    assert False, f"Missing Link {link1.to_node}->{link1.from_node}"
        for link in self.links:
            assert link.to_node in self.nodes
            assert link.from_node in self.nodes
            link.to_node.referenced = True
            link.from_node.referenced = True
        for node in self.nodes:
            assert node.visited == False
            for link in node.links:
                assert link in self.links
                assert link.cost is not None
                link.referenced = True
        for link in self.links:
            assert link.referenced
            del link.referenced
        for node in self.nodes:
            assert node.referenced
            del node.referenced


def make_graph(num_vertices: int, num_edges: int, connected=True, directed=True):
    def link_exists(from_node, to_node):
        for link in links:
            # fmt: off
            if link.from_node == from_node and \
               link.to_node == to_node:
                return True
        return False

    assert not (connected and num_edges < (num_vertices - 1))
    nodes: List[Node] = [Node(i + 1) for i in range(num_vertices)]
    links: List[Link] = []

    count_edges = num_edges
    while count_edges:
        from_node = choice(nodes)
        nodes_remain = nodes[:]
        nodes_remain.remove(from_node)
        to_node = choice(nodes_remain)
        if link_exists(from_node, to_node):
            continue
        cost = random()
        link1 = Link(from_node, to_node, cost)
        links.append(link1)
        if not directed:
            link2 = Link(to_node, from_node, cost)
            links.append(link2)
            link1.set_cmpl(link2)
            link2.set_cmpl(link1)
        count_edges -= 1

    if connected:
        while True:
            linked_nodes = set()
            for link in links:
                linked_nodes.add(link.from_node)
                linked_nodes.add(link.to_node)
            island_nodes = set(nodes) - linked_nodes
            if len(island_nodes) == 0:
                break
            for node in island_nodes:
                if directed:
                    link = choice(links)
                    if random() < 0.5:
                        link.from_node = node
                    else:
                        link.to_node = node
                else:
                    link1 = choice(links)
                    link2 = link1.cmpl
                    link1.to_node = node
                    link2.from_node = node
                    node.links.append(link2)
    for link in links:
        link.from_node.links.append(link)
    return Graph(nodes, links)


def make_sp_graph(connected=True):
    from shortest_path import SPNode, SPLink

    node_string = "ABCDEFGHIJKLMNOP" if connected else "ABCDEFGHIJKLMNOPQ"
    node_labels = [label for label in node_string]
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
        "Q": [("A", 1), ("P", 1)],
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


if __name__ == "__main__":
    graph = make_graph(5, 7, directed=True)
    print(graph)
    graph = make_graph(5, 7, directed=False)
    print(graph)
    graph = make_sp_graph(connected=True)
    graph = make_sp_graph(connected=False)
    print(graph)
