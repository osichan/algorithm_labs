class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def inorder_traversal(node):
    values = []
    if node is not None:
        values += inorder_traversal(node.left)
        values.append(node)
        values += inorder_traversal(node.right)
    return values


def find_successor(tree: BinaryTree, node) -> BinaryTree:
    inorder_array = inorder_traversal(tree)
    for i in range(len(inorder_array)):
        if inorder_array[i].value == node:
            if i < len(inorder_array) - 1:
                return inorder_array[i + 1]
    return BinaryTree("Not Found")


root = BinaryTree(10)
root.left = BinaryTree(5, BinaryTree(3), BinaryTree(7))
root.right = BinaryTree(15, None, BinaryTree(20, BinaryTree(25)))


successor = find_successor(root, 25)
print(successor.value)
