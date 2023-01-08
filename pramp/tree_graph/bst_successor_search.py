"""
BST Successor Search
In a Binary Search Tree (BST), an Inorder Successor of a node is defined as the node with the smallest key greater than the key of the input node
(see examples below). Given a node inputNode in a BST, you’re asked to write a function findInOrderSuccessor that returns the Inorder Successor of inputNode.
If inputNode has no Inorder Successor, return null.
            20
           /  \
          9    25
         / \
        5   12
           /  \
         11    14


input = node 11
output = node 12
input = node 9
output = node 11
input = node 14
output = node 20
"""

"""
Solution:
If a node x has a right child, its successor is the minimal node of its right sub-tree.
In other words, the node’s successor is the leftmost descendant of its right child in this case.
Because, after visiting x, the traversal procedure will process the right sub-tree of x,
  and the first to visit there is its leftmost leaf.

If x has no right child, its in-order successor is located above it in the tree, among its ancestors. While unfolding the recursive calls, the in-order traversal function will first visit the node whose left child was the most recent input. So, the x‘s successor is the parent of the \boldsymbol{x}‘s youngest ancestor that is a left child.
Time Complexity: in both cases where either inputNode has a right child or doesn’t have one,
 we are visiting only O(H) number of nodes, where H is the height of the BST.
  For a balanced BST, since H = log(N), where N is the number of nodes in the BST, the time complexity is O(log(N)).
   For an unbalanced BST, the time complexity is O(N).

Space Complexity: throughout the entire algorithm we used only a constant amount of space, hence the space complexity is O(1).

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

    def find_in_order_successor(self, input_node):
        if input_node.right:
            # return the node with minimum key in the right subtree
            return self.find_min_key_within_tree(input_node.right)

        child = input_node
        ancestor = input_node.parent

        # travel up using the parent pointer until you see
        # a node which is the left child of its parent. The parent
        # of such a node is successorNode.
        while ancestor and ancestor.right == child:
            child = ancestor
            ancestor = child.parent
        return ancestor

    def find_min_key_within_tree(self, input_node):
        while input_node.left:
            input_node = input_node.left
        return input_node

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

    # Return a reference to a node in the BST by its key.
    # Use this method when you need a node to test your
    # findInOrderSuccessor function on
    def get_node_by_key(self, key):
        current_node = self.root
        while current_node is not None:
            if key == current_node.key:
                return current_node

            if key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return None


def main():
    # Create a Binary Search Tree
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(9)
    bst.insert(25)
    bst.insert(5)
    bst.insert(12)
    bst.insert(11)
    bst.insert(14)

    # Get a reference to the node whose key is 9
    assert bst.find_in_order_successor(bst.get_node_by_key(11)) == bst.get_node_by_key(12)
    assert bst.find_in_order_successor(bst.get_node_by_key(9)) == bst.get_node_by_key(11)
    assert bst.find_in_order_successor(bst.get_node_by_key(14)) == bst.get_node_by_key(20)
    assert bst.find_in_order_successor(bst.get_node_by_key(25)) is None


if __name__ == '__main__':
    main()
