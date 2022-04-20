'''
BFS and Find Hops (Distance) from Node
'''

from collections import deque
from graph_utils import *

def bfs(node: Node):
    visited = set()
    q = deque([node])
    while q:
        node = q.pop()
        print(node, end=', ')
        visited.add(node)
        node.visited = True
        for link in node.links:
            if not link.to_node.visited:
                q.appendleft(link.to_node)
    print()
    for node in visited:
        node.visited = False

g = make_graph(5, 6)
print(g)
bfs(g.nodes[0])

def hops_from(node: Node):
    visited = set()
    hops_nodes = {}
    hops = 0
    q = deque([node])
    q_tmp = deque()
    while q or q_tmp:
        if not q:
            q.extendleft(q_tmp)
            q_tmp.clear()
            hops += 1
        node = q.pop()
        hops_nodes[node] = hops
        visited.add(node)
        node.visited = True
        for link in node.links:
            if not link.to_node.visited:
                q_tmp.appendleft(link.to_node)
    for node in visited:
        node.visited = False
    return hops_nodes

# g = make_graph(5, 6)
# print(g)
print(hops_from(g.nodes[0]))
