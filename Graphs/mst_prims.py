"""
Minimum Spanning Tree (MST) using Prim's Algorithm
ST: Tree that visits every node in a graph
MST: ST with lowest possible total-cost
"""

from graph_utils import *

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

    print("Unreachable Nodes:", set(graph.nodes) - set(min_nodes))

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


# g = make_graph(5, 7, directed=False)
# g = make_sp_graph(connected=True)
g = make_sp_graph(connected=False)
print(g)
print(mst_prims(g, 0))
