"""
Find Shortest Paths using Label Setting
"""

from math import inf
from typing import Optional, List
from graph_utils import Node, Link, Graph, make_sp_graph


class SPNode(Node):
    def __init__(self, label, links: List["SPLink"] = None, visited=False):
        super().__init__(label, links, visited)
        self.from_link: Optional[Link] = None
        self.distance = +inf


class SPLink(Link):
    def __init__(self, from_node: SPNode, to_node: SPNode, cost=0):
        super().__init__(from_node, to_node, cost)
        self.distance = +inf


def shortest_path(graph: Graph, start_node_idx, end_node_idx):
    def remove_inside_links() -> None:
        remove = []
        for link in sp_links:
            if link.to_node.distance < inf:
                remove.append(link)
        for link in remove:
            sp_links.remove(link)

    def find_min_dist_link() -> SPLink:
        for link in sp_links:
            link.distance = link.from_node.distance + link.cost
        return min(sp_links, key=lambda link: link.distance)

    end_node = graph.nodes[end_node_idx]
    start_node = graph.nodes[start_node_idx]
    start_node.distance = 0
    sp_links = start_node.links[:]

    while sp_links:
        min_link = find_min_dist_link()
        min_link.to_node.from_link = min_link
        min_link.to_node.distance = min_link.distance
        if min_link.to_node is end_node:
            break
        sp_links.extend(min_link.to_node.links)
        remove_inside_links()

    # Shortest Path Tree (through to end node)
    for node in graph.nodes:
        print(node.label, node.distance, node.from_link)

    # Shortest Path from Start Node to End Node
    print(end_node, end="->")
    while node is not start_node:
        node = node.from_link.from_node
        print(node, end="->")
    print()


if __name__ == "__main__":
    g = make_sp_graph(connected=True)
    print(g)
    shortest_path(g, 0, 15)
