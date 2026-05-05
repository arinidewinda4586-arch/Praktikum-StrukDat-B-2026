class Node:
    """Representasi satu node dalam binary tree"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    """Implementasi kelas Binary Tree"""
    def __init__(self):
        self.root = None

    def insert(self, data):
        # langkah 1
        new = Node(data)

        # langkah 2
        if self.root is None:
            self.root = new
            return

        # langkah 3
        P = self.root
        Q = self.root

        # langkah 4
        while Q is not None and new.data != P.data:

            # langkah 5
            P = Q

            # langkah 6
            if new.data < P.data:
                Q = P.left
            else:
                Q = P.right

        # langkah 7
        if new.data == P.data:
            print("data sama")
            return

        # langkah 8
        if new.data < P.data:
            P.left = new
        else:
            P.right = new


# traversal inorder
def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.data, end=" ")
        in_order(node.right)


# membuat tree
bst = BinaryTree()
bst.insert(12)
bst.insert(9)
bst.insert(99)
bst.insert(67)
bst.insert(35)

in_order(bst.root)


def insert_left(self, parent_node, data):
    if parent_node.left is None:
        parent_node.left = Node(data)
    else:
        new_node = Node(data)
        new_node.left = parent_node.left
        parent_node.left = new_node


def insert_right(self, parent_node, data):
    if parent_node.right is None:
        parent_node.right = Node(data)
    else:
        new_node = Node(data)
        new_node.right = parent_node.right
        parent_node.right = new_node