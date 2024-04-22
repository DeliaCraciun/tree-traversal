from node import Node


class Tree:
    """ Tree class for binary tree """

    def __init__(self):
        """ Constructor for Tree class """
        self.root = None

    def getRoot(self):
        """ Method for get root of the tree """
        return self.root

    def add(self, data):
        """ Method for add data to the tree """
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        """Method for add data to the tree

        Args:
            data (int): data to add

        Returns:
            None
        """
        if data < node.data:
            if node.left is not None:
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right is not None:
                self._add(data, node.right)
            else:
                node.right = Node(data)

    def find(self, data):
        """Method for find data in the tree

        Args:
            data (int): data to find

        Returns:
            Node: node with data
        """
        if self.root is not None:
            return self._find(data, self.root)
        else:
            return None

    def _find(self, data, node):
        if data == node.data:
            return node
        elif (data < node.data and node.left is not None):
            return self._find(data, node.left)
        elif (data > node.data and node.right is not None):
            return self._find(data, node.right)

    def deleteTree(self):
        """
        Resets the tree to an empty state.

        This method sets the root of the tree to None, effectively removing all elements and thus 'deleting' the tree.
        """
        self.root = None

    def printTree(self):
        """
        Prints the contents of the tree in an in-order traversal.

        This method prints each node's data in the tree. It will start from the leftmost node, moving to the root,
        and finally to the rightmost node, reflecting an in-order traversal.
        If the tree is empty, it will not print anything.
        """
        if self.root is not None:
            self._printInorderTree(self.root)


    def deleteTree(self):
        """
        Resets the tree to an empty state.

        This method sets the root of the tree to None, effectively removing all elements and thus 'deleting' the tree.
        """
        self.root = None

    def printTree(self):
        """
        Prints the contents of the tree in an in-order traversal.

        This method prints each node's data in the tree. It will start from the leftmost node, moving to the root,
        and finally to the rightmost node, reflecting an in-order traversal.
        If the tree is empty, it will not print anything.
        """
        if self.root is not None:
            self._printInorderTree(self.root)

    def _printInorderTree(self, node):
        """
        A helper method that performs an in-order traversal of the tree starting from a given node.

        This method is called recursively to visit a node's left subtree, then the node itself, and finally its right subtree.
        This ensures that the nodes are visited in non-decreasing order.

        Parameters:
        node (TreeNode): The node from which the in-order traversal begins.

        Note: This method is intended to be private and is used internally by the printTree method.
        """
        if node is not None:
            self._printInorderTree(node.left)
            print(str(node.data) + ' ')
            self._printInorderTree(node.right)

    def _printPreorderTree(self, node):
        """
        Recursively performs a pre-order traversal from 'node', printing data before visiting left and right children.
        This is intended for internal use to explore roots before leaves.
        """
        if node is not None:
            print(node.data, end=" ")
            self._printPreorderTree(node.left)
            self._printPreorderTree(node.right)

    def _printPostorderTree(self, node):
        """
        Recursively performs a post-order traversal from 'node', printing data after visiting left and right children.
        This method is ideal for operations requiring subtree processing first.
        """
        if node is not None:
            self._printPostorderTree(node.left)
            self._printPostorderTree(node.right)
            print(node.data, end=" ")


    def trial2(self):
        """Trial method
            
        Returns:
            None
        """
        print("This is a useless method")