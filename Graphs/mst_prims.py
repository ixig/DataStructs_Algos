"""
Minimum Spanning Tree (MST) using Prim's Algorithm
"""

from copy import copy
from typing import Tuple
from graph_utils import *

def mst_prims(graph: Graph, node_idx=0):
    def find_link(to_node: Node, from_node: Node) -> Link:
        for link in from_node.links:
            if link.to_node is to_node:
                return link
        return None

    def lowest_cost_link() -> Tuple[Node, Tuple[Link, Link]]:
        out_links = []
        for node in mst_nodes:
            for link in node.links:
                out_links.append((node, link))
        from_node, min_link = min(out_links, key=lambda tup: tup[1].cost)
        min_link1 = min_link
        min_link2 = find_link(from_node, min_link.to_node)
        return min_link.to_node, (min_link1, min_link2)

    node = graph.nodes[node_idx]
    mst_nodes = [node]
    mst_links = []

    for _ in range(len(graph.nodes) - 1):
        min_node, min_link_pair = lowest_cost_link()
        new_node = copy(min_node)
        new_node.links = [*min_link_pair]
        mst_nodes.append(new_node)
        mst_links.extend(min_link_pair)

    return mst_nodes, mst_links


g = make_graph(5, 7, directed=False)
print(g)
print(mst_prims(g, 0))
