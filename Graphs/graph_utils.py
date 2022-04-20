"""'
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


class Link:
    def __init__(self, from_node: Node, to_node: Node, cost=0):
        self.from_node = from_node
        self.to_node = to_node
        self.cost = cost

    def __repr__(self):
        return f"{self.from_node}->{self.to_node} <{self.cost:.3f}>"


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
                s += f"{link.to_node}/{link.cost:.3f}, "
            s = s.rstrip(", ") + "\n"
        return s

    def check(self):
        if not self.directed:
            for link1 in self.links:
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
        links.append(Link(from_node, to_node, cost))
        if not directed:
            links.append(Link(to_node, from_node, cost))
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
                    for link2 in links:
                        # fmt: off
                        if link2.from_node is link1.to_node and \
                           link2.to_node is link1.from_node:
                            link2.from_node.links.remove(link2)
                            break
                    else:
                        assert False
                    link1.to_node = node
                    link2.from_node = node
                    node.links.append(link2)
    for link in links:
        link.from_node.links.append(link)
    return Graph(nodes, links)

if __name__ == "__main__":
    graph = make_graph(5, 7, directed=True)
    print(graph)
    graph = make_graph(5, 7, directed=False)
    print(graph)
