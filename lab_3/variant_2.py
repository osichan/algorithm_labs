class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def height(node):
    if node is not None:
        left_height = height(node.left)
        right_height = height(node.right)
        return 1 + max(left_height, right_height)
    return 0

def is_tree_balanced(node):
    if node is None:
        return True  # An empty tree is balanced

    left_height = height(node.left)
    right_height = height(node.right)

    if abs(left_height - right_height) <= 1 and is_tree_balanced(node.left) and is_tree_balanced(node.right):
        return True

    return False

def check_balance_recursively(node):
    if node is None:
        return True

    if is_tree_balanced(node):
        return check_balance_recursively(node.left) and check_balance_recursively(node.right)
    else:
        return False


root = BinaryTree(50)
root.left=BinaryTree(17)
root.left.left=BinaryTree(9)
root.left.left.right=BinaryTree(14)
root.left.left.right.left=BinaryTree(12)
root.left.right=BinaryTree(23)
root.left.right.left=BinaryTree(19)
root.right=BinaryTree(76)
root.right.left=BinaryTree(54)
root.right.left.right=BinaryTree(72)
root.right.left.right.left=BinaryTree(67)


print(check_balance_recursively(root))

root_1 = BinaryTree(50)
root_1.left=BinaryTree(17)
root_1.left.left=BinaryTree(12)
root_1.left.left.left=BinaryTree(9)
root_1.left.left.right=BinaryTree(14)
root_1.left.right=BinaryTree(23)
root_1.left.right.left=BinaryTree(19)
root_1.right=BinaryTree(72)
root_1.right.left=BinaryTree(54)
root_1.right.left.right =BinaryTree(67)
root_1.right.right=BinaryTree(76)
print(check_balance_recursively(root_1))