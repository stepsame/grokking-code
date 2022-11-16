"""
Sales Path
The car manufacturer Honda holds their distribution system in the form of a tree (not necessarily binary).
The root is the company itself, and every node in the tree represents a car distributor that receives cars from the parent node
and ships them to its children nodes. The leaf nodes are car dealerships that sell cars direct to consumers.
In addition, every node holds an integer that is the cost of shipping a car to it.
Take for example the tree below:
                0
           /    |    \
        5       3       6
       /       / \     / \
      4       2   0   1   5
             /   /
            1   10
             \
              1

A path from Honda’s factory to a car dealership, which is a path from the root to a leaf in the tree, is called a Sales Path.
The cost of a Sales Path is the sum of the costs for every node in the path.
For example, in the tree above one Sales Path is 0→3→0→10, and its cost is 13 (0+3+0+10).

Honda wishes to find the minimal Sales Path cost in its distribution tree.
Given a node rootNode, write a function getCheapestCost that calculates the minimal Sales Path cost in the tree.

Implement your function in the most efficient manner and analyze its time and space complexities.

For example:

Given the rootNode of the tree in diagram above

Your function would return:

7 since it’s the minimal Sales Path cost (there are actually two Sales Paths in the tree whose cost is 7: 0→6→1 and 0→3→2→1→1)

"""

"""
Solution: 
bfs or dfs traverse the tree, and when meet a leaf node, record the minimal cost.

Time Complexity: DFS is O(N) BFS is O(N)
Space Complexity: DFS is O(N) BFS is O(N)

"""


class Node:
    def __init__(self, children, cost):
        self.children = children
        self.cost = cost

    def __repr__(self):
        return f'<{self.cost}>'


def solution(root):
    queue = [(root, root.cost)]
    min_cost = float('inf')
    while queue:
        print(queue)
        node, path_cost = queue.pop(0)
        if not node.children:
            if path_cost < min_cost:
                min_cost = path_cost
        else:
            for child in node.children:
                queue.append((child, path_cost + child.cost))
    return min_cost


def main():
    """

                0
           /    |    \
        5       3       6
       /       / \     / \
      4       2   0   1   5
             /   /
            1   10
             \
              1
    """
    k = Node(None, 1)
    j = Node(None, 10)
    i = Node([k], 1)
    h = Node(None, 5)
    g = Node(None, 1)
    f = Node([j], 0)
    e = Node([i], 2)
    d = Node(None, 4)
    c = Node([g, h], 6)
    b = Node([e, f], 3)
    a = Node([d], 5)
    root = Node([a, b, c], 0)
    assert solution(root) == 7


if __name__ == '__main__':
    main()
