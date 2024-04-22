import unittest
from node import Node  # Ensure this is the correct import statement for your Node class
from tree import Tree
class TestTree(unittest.TestCase):

    def setUp(self):
        """ Set up for test """
        self.tree = Tree()
        self.tree.add(8)
        self.tree.add(3)
        self.tree.add(10)
        self.tree.add(1)
        self.tree.add(6)
        self.tree.add(4)
        self.tree.add(7)
        self.tree.add(14)
        self.tree.add(13)

    def test_find_existing_node(self):
        """ Test finding an existing node """
        result = self.tree.find(6)
        self.assertIsNotNone(result)
        self.assertEqual(result.data, 6)
        self.assertIsInstance(result, Node)

    def test_find_non_existing_node(self):
        """ Test finding a non-existing node """
        result = self.tree.find(99)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
