"""
Largest Smaller BST Key
Given a root of a Binary Search Tree (BST) and a number num, implement an efficient function findLargestSmallerKey that finds the largest key in the tree
that is smaller than num. If such a number doesn’t exist, return -1. Assume that all keys in the tree are nonnegative.
For num = 17 and the binary search tree below:
            20
           /  \
          9    25
         / \
        5   12
           /  \
         11    14
Your function would return: 14 since it’s the largest key in the tree that is still smaller than 17.
"""

"""
Solution:
Part 1: Traversing the tree
    A node in a binary search tree is larger than all keys in its left subtree and smaller than all keys i its right subtree.
    Starting from the root, for each node we choose its left or its right child as the next step,
    based on a comparison between that node's key and num: If the current node holds a key smaller than num,
     we proceed to its right subtree looking for larger keys. 
    Otherwise, we proceed to its left subtree looking for smaller keys.

Part 2: Finding the key
    During this iteration, when the current key is smaller than num,
    we store it as our result and keep looking for a larger key that is still smaller than num.
    It's important to understand why we always store the last key without comparing it to the value stored beforehand.
    If we have stored a key before, then it means we have chosen to continue down the key’s right subtree.
    Therefore, all subsequent keys will be larger than any previously stored keys.

Time Complexity: We scan the tree once from the root to the the leaves and do a constant number of actions for each node. if the tree is balanced the complexity is O(log(N)). Otherwise, it could be up to O(N).
Space Complexity: Throughout the entire algorithm we used only a constant amount of space, hence the space complexity is O(1).

"""


# A node
class Node:
    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


# A binary search tree
class BinarySearchTree:
    # Constructor to create a new BST
    def __init__(self):
        self.root = None

    def find_largest_smaller_key(self, num):
        result = -1
        node = self.root
        while node:
            if node.key < num:
                result = node.key
                node = node.right
            else:
                node = node.left
        return result


    # Given a binary search tree and a number, inserts a
    # new node with the given number in the correct place
    # in the tree. Returns the new root pointer which the
    # caller should then use(the standard trick to avoid
    # using reference parameters)
    def insert(self, key):
        # 1) If tree is empty, create the root
        if self.root is None:
            self.root = Node(key)
            return

        # 2) Otherwise, create a node with the key
        #    and traverse down the tree to find where to
        #    to insert the new node
        current_node = self.root
        new_node = Node(key)

        while current_node is not None:
            if key < current_node.key:
                if current_node.left is None:
                    current_node.left = new_node
                    new_node.parent = current_node
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    new_node.parent = current_node
                    break
                else:
                    current_node = current_node.right


def main():
    bst = BinarySearchTree()

    # Create the tree given in the above diagram
    bst.insert(20)
    bst.insert(9)
    bst.insert(25)
    bst.insert(5)
    bst.insert(12)
    bst.insert(11)
    bst.insert(14)

    assert bst.find_largest_smaller_key(17) == 14


if __name__ == '__main__':
    main()
