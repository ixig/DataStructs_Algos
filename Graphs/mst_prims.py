"""
Minimum Spanning Tree (MST) using Prim's Algorithm
"""

from graph_utils import *

def mst_prims(graph: Graph, node_idx=0):
    def lowest_cost_link() -> Link:
        links = []
        for node in min_nodes:
            links.extend([link for link in node.links if link.to_node not in min_nodes])
        min_link = min(links, key=lambda link: link.cost)
        return min_link

    node = graph.nodes[node_idx]
    min_nodes = [node]
    min_links = []

    for _ in range(len(graph.nodes) - 1):
        min_link_out = lowest_cost_link()
        min_links.append(min_link_out)
        min_nodes.append(min_link_out.to_node)

    # make new MST graph
    mst_nodes, mst_links = [], []
    old2new_nodes = {}
    for old_node in min_nodes:
        new_node = old_node.copy()
        mst_nodes.append(new_node)
        old2new_nodes[old_node] = new_node
    for old_link in min_links:
        new_link = old_link.copy(
            old2new_nodes[old_link.from_node], old2new_nodes[old_link.to_node]
        )
        mst_links.append(new_link)
        new_link.from_node.links.append(new_link)

    return Graph(mst_nodes, mst_links)


g = make_graph(5, 7, directed=False)
print(g)
print(mst_prims(g, 0))
