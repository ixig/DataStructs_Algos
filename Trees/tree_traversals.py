from collections import deque
from tree_utils import *

def preorder(node: Node):
    print(node.value, end=', ')
    for child in (node.left, node.right):
        if child:
            preorder(child)

def postorder(node: Node):
    for child in (node.left, node.right):
        if child:
            postorder(child)
    print(node.value, end=', ')

def inorder(node: Node):
    if node.left:
        inorder(node.left)
    print(node.value, end=', ')
    if node.right:
        inorder(node.right)

def bfs(node: Node):
    q = deque([node])
    while q:
        node = q.pop()
        for child in (node.left, node.right):
            if child:
                q.appendleft(child)
        print(node.value, end=', ')

tree = make_tree(6)
print_tree(tree)

print('pre:  ', end=''); preorder(tree); print()
print('post: ', end=''); postorder(tree); print()
print('ino:  ', end=''); inorder(tree); print()

print('BFS:  ', end=''); bfs(tree); print()
