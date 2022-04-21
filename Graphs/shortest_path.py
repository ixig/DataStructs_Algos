"""
Find Shortest Paths using Label Setting
"""

from math import inf
from typing import Optional, List
from graph_utils import Node, Link, Graph, make_sp_graph


class SPNode(Node):
    def __init__(self, label, links: List["SPLink"] = None, visited=False):
        super().__init__(label, links, visited)
        self.shortest: Optional[Link] = None
        self.distance = +inf


class SPLink(Link):
    def __init__(self, from_node: "SPNode", to_node: "SPNode", cost=0):
        super().__init__(from_node, to_node, cost)
        self.distance = +inf


def shortest_path(graph: Graph, start_node_idx, end_node_idx):
    def remove_inside_links(links) -> None:
        remove = []
        for link in links:
            if link.to_node.distance < inf:
                remove.append(link)
        for link in remove:
            links.remove(link)

    def shortest_link(links) -> SPLink:
        for link in links:
            link.distance = link.from_node.distance + link.cost
        return min(links, key=lambda link: link.distance)

    start_node = graph.nodes[start_node_idx]
    start_node.distance = 0
    links = start_node.links[:]

    while links:
        min_link = shortest_link(links)
        min_link.to_node.shortest = min_link
        min_link.to_node.distance = min_link.distance
        links.extend(min_link.to_node.links)
        remove_inside_links(links)

    # Shortest Path Tree
    for node in graph.nodes:
        print(node.label, node.distance, node.shortest)

    # Shortest Path from Start Node to End Node
    node = graph.nodes[end_node_idx]
    print(node, end="->")
    while node is not start_node:
        node = node.shortest.from_node
        print(node, end="->")
    print()


if __name__ == "__main__":
    g = make_sp_graph()
    print(g)
    shortest_path(g, 0, 15)
