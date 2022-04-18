"""'
Helper Utilities for Creating Graphs
"""
from typing import List, Union
from random import choice, random, randint


class NodeLinks:
    def __init__(
        self, label, out_links: List["Link"] = None, in_links: List["Link"] = None, visited=False
    ):
        self.label = label
        self.out_links = out_links if out_links is not None else []
        self.in_links = in_links if in_links is not None else []
        self.visited = visited

    def __repr__(self):
        return str(self.label)


class Link:
    def __init__(self, from_node: NodeLinks, to_node: NodeLinks, cost=0):
        self.from_node = from_node
        self.to_node = to_node
        self.cost = cost

    def __repr__(self):
        return f"{self.from_node}->{self.to_node} <{self.cost:.2f}>"


class NodeNeighbors:
    def __init__(self, label, neighbors=None, visited=False):
        self.label = label
        self.neighbors = neighbors if neighbors is not None else []
        self.visited = visited

    def __repr__(self):
        return str(self.label)


NodeType = Union[NodeLinks, NodeNeighbors]


class GraphNodeLinks:
    def __init__(self, nodes: List[NodeLinks], links: List[Link]):
        self.nodes = nodes
        self.links = links

    def __str__(self):
        s = ""
        for node in self.nodes:
            s += f"{node.label}: O[ "
            for link in node.out_links:
                s += f"{link.to_node}/{link.cost:.2f}, "
            s = s.rstrip(", ") + " ], I[ "
            for link in node.in_links:
                s += f"{link.from_node}/{link.cost:.2f}, "
            s = s.rstrip(", ") + " ]\n"
        return s


def make_graph(num_vertices: int, num_edges: int, connected=True):
    def link_exists(from_node, to_node):
        for link in links:
            if link.from_node == from_node and link.to_node == to_node:
                return True
        return False

    assert not (connected and num_edges < (num_vertices - 1))
    nodes: List[NodeLinks] = [NodeLinks(i + 1) for i in range(num_vertices)]
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
        links.append(Link(from_node, to_node, cost))
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
                if random() < 0.5:
                    choice(links).from_node = node
                else:
                    choice(links).to_node = node

    for link in links:
        link.from_node.out_links.append(link)
        link.to_node.in_links.append(link)
    return GraphNodeLinks(nodes, links)


if __name__ == "__main__":
    graph = make_graph(5, 7)
    print(graph)
