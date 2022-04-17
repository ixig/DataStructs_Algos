from tree_utils import *
from math import inf

def find(node: Node, value: int, parent=None):
    if node is None:
        return None, parent
    elif node.value == value:
        return node, parent
    elif value < node.value:
        return find(node.left, value, node)
    else:
        return find(node.right, value, node)

def insert(node: Node, value: int):
    if value > node.value:
        if not node.right:
            node.right = Node(value, None, None)
        else:
            insert(node.right, value)
    else:
        if not node.left:
            node.left = Node(value, None, None)
        else:
            insert(node.left, value)

def find_rightmost(node: Node, parent=None):
    if node.right is None:
        return node, parent
    else:
        return find_rightmost(node.right, node)

def remove(node: Node, value: int):

    def replace(parent: Node, old: Node, new: Node):
        if parent.left is old:
            parent.left = new
        elif parent.right is old:
            parent.right = new
        else:
            assert False

    super_root = Node(inf, node, None)
    remove, remove_parent = find(super_root, value)
    if remove is None:
        print(f'ERROR: {value} not found!') 
        return
    if not remove.left and not remove.right:  # node has no children
        replace(remove_parent, remove, None)
    elif remove.left and remove.right:  # node has two chidren
        if remove.left.right is None:  # node's left child has no right child
            replace(remove_parent, remove, remove.left)
        else:  # nodes's left child has a right child (!!!)
            rightmost_node, rightmost_parent = find_rightmost(remove.left)
            remove.value = rightmost_node.value
            if rightmost_node.left:  # rightmost node has one child (has to be left)
                replace(rightmost_parent, rightmost_node, rightmost_node.left)
            else:  # rightmost node has no childern
                replace(rightmost_parent, rightmost_node, None)
    elif remove.left:  # node has only left child
        replace(remove_parent, remove, remove.left)
    else:  # node has only right child
        replace(remove_parent, remove, remove.right)
    return super_root.left


from random import choice

if True:
    tree, tree_vals = make_tree(10, unique_vals=True, ret_vals=True, sorted=True)
    print_tree(tree)
    print(tree_vals)

if False:
    value = choice(list(tree_vals))
    print(value, ':', find(tree, value))
    print(value+1, ':', find(tree, value+1))

if True:
    def insert_test(tree: Node, tree_vals):
        while True:
            value = randint(10, 99)
            if value not in tree_vals:
                insert(tree, value)
                print(f'Inserted {value}')
                break

    insert_test(tree, tree_vals)
    print_tree(tree)
    assert check_sorted(tree)

if False:
    print('>', find_rightmost(tree).value)

if False:
    for _ in range(50):
        print('.', end='')
        tree, tree_vals = make_tree(10, unique_vals=True, ret_vals=True, sorted=True)
        value = choice(list(tree_vals))
        tree = remove(tree, value)
        assert find(tree, value)[0] is None
        assert check_sorted(tree)
