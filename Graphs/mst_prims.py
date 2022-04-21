"""
Minimum Spanning Tree (MST) using Prim's Algorithm
ST: Tree that visits every node in a graph
MST: ST with lowest possible total-cost
"""

from graph_utils import *


def make_new_graph(nodes, links):
    new_nodes, new_links = [], []
    old2new_nodes = {}
    for old_node in nodes:
        new_node = old_node.copy()
        new_nodes.append(new_node)
        old2new_nodes[old_node] = new_node
    for old_link in links:
        new_link = old_link.copy(
            old2new_nodes[old_link.from_node], old2new_nodes[old_link.to_node]
        )
        new_links.append(new_link)
        new_link.from_node.links.append(new_link)
    return Graph(new_nodes, new_links)


def mst_prims(graph: Graph, node_idx=0):
    def find_min_link() -> Link:
        links = []
        for node in min_nodes:
            links.extend([link for link in node.links if link.to_node not in min_nodes])
        if links:
            min_link = min(links, key=lambda link: link.cost)
            return min_link
        else:
            return None

    min_nodes = [graph.nodes[node_idx]]
    min_links = []

    for _ in range(len(graph.nodes) - 1):
        min_link = find_min_link()
        if not min_link:
            break
        min_links.append(min_link)
        min_nodes.append(min_link.to_node)

    print("Unreachable Nodes:", set(graph.nodes) - set(min_nodes), end=" ; ")
    mst_cost = 0
    for link in min_links:
        mst_cost += link.cost
    print("MST Cost:", mst_cost)

    return make_new_graph(min_nodes, min_links)


# g = make_graph(5, 7, directed=False)
# g = make_sp_graph(connected=True)
g = make_sp_graph(connected=False)
print(g)
print(mst_prims(g, 0))
