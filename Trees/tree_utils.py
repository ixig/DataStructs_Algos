from random import choice, randint

class Node:
    def __init__(self, value, left, right, min_value=None, max_value=None):
        self.value = value
        self.left = left
        self.right = right
        self.min_value = min_value
        self.max_value = max_value

def _make_tree(num_nodes, min_val, max_val, unique_vals, ret_vals, sorted):

    def make_node(min_val=min_val, max_val=max_val):
        if min_val > max_val:
            raise Exception((min_val, max_val))
        while True:
            value = randint(min_val, max_val)
            if (not unique_vals) or (value not in node_values):
                break
        node_values.add(value)
        return Node(value, None, None, min_val, max_val)

    node_values = set()
    root = make_node()
    nodes = [root]
    while num_nodes:
        node = choice(nodes)
        if node.left and node.right:
            continue
        lr = choice(('left', 'right'))
        if node.left or (not node.right and lr == 'right'):
            if sorted:
                new_node = make_node(
                    min_val=(node.value + 1),
                    max_val=node.max_value)
            else:
                new_node = make_node()
            node.right = new_node
        elif node.right or (not node.left and lr == 'left'):
            if sorted:
                new_node = make_node(
                    min_val=node.min_value,
                    max_val=(node.value - 1))
            else:
                new_node = make_node()
            node.left = new_node
        nodes.append(new_node)
        num_nodes -= 1
    if ret_vals:
        return root, node_values
    else:
        return root

def make_tree(num_nodes, min_val=10, max_val=99, unique_vals=False, ret_vals=False, sorted=False):
    while True:
        try:
            return _make_tree(num_nodes, min_val, max_val, unique_vals, ret_vals, sorted)
        except:
            continue
    
def print_tree(node, level=0):
    if level == 0: print('='*20)
    if node != None:
        print_tree(node.right, level + 1)
        print(' ' * 3 * level + '- ' + str(node.value))
        print_tree(node.left, level + 1)
    if level == 0: print('='*20)

def check_sorted(node):
    if not node or (not node.left and not node.right):
        return True
    else:
        if node.left and node.left.value > node.value:
            return False
        if node.right and node.right.value < node.value:
            return False
        return check_sorted(node.left) and check_sorted(node.right)

if __name__ == '__main__':
    for _ in range(50):
        tree, tree_vals = make_tree(6, unique_vals=True, ret_vals=True, sorted=True)
        assert check_sorted(tree)
