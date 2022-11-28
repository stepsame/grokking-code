"""
H-Tree Construction
An H-tree is a geometric shape that consists of a repeating pattern resembles the letter “H”.
It can be constructed by starting with a line segment of arbitrary length, drawing two segments of the same length
at right angles to the first through its endpoints, and continuing in the same vein,
reducing (dividing) the length of the line segments drawn at each stage by √2.
Write a function drawHTree that constructs an H-tree, given its center (x and y coordinates), a starting length, and depth.
Assume that the starting line is parallel to the X-axis.
Use the function drawLine provided to implement your algorithm.
In a production code, a drawLine function would render a real line between two points.
However, this is not a real production environment, so to make things easier, implement drawLine such that it simply prints its arguments
(the print format is left to your discretion).

"""
from collections import namedtuple

# pip install matplotlib
import matplotlib.pyplot as plt

"""
Solution:
We will start from the center point. Compute the coordinates of the 4 tips of the H.
Then we shall draw the 3 line segments of the H, i.e. left and right vertical of the H, and the connection of the two vertical segments.
We will update the length and recursively draw 4 half-size H-trees of order one less than the current depth.

Time Complexity:
every call of drawHTree invokes 4 calls of drawHTree until depth reaches to 0.
So the recursive call stack will be like a 4-ary tree. So the time complexity will be O(4^D).

Space Complexity: recursive calls add overhead since we store them in the execution stack.
The max length of the stack is equal to the tree's depth, so the Space Complexity will be O(D)

"""
Point = namedtuple('Point', ['x', 'y'])
fig, ax = plt.subplots()

def draw_line(a, b):
    plt.plot([a.x, b.x], [a.y, b.y])
    # print(a, b)


def draw_htree(x, y, length, depth):
    if depth == 0:
        return

    print('draw ', x, y, length, depth)

    left_x = x - length / 2.0
    right_x = x + length / 2.0
    top_y = y + length / 2.0
    bottom_y = y - length / 2.0

    draw_line(Point(x=left_x, y=top_y), Point(x=left_x, y=bottom_y))
    draw_line(Point(x=right_x, y=top_y), Point(x=right_x, y=bottom_y))
    draw_line(Point(x=left_x, y=y), Point(x=right_x, y=y))

    new_length = length / (2 ** (1/2))
    draw_htree(left_x, top_y, new_length, depth - 1)
    draw_htree(left_x, bottom_y, new_length, depth - 1)
    draw_htree(right_x, top_y, new_length, depth - 1)
    draw_htree(right_x, bottom_y, new_length, depth - 1)
    # plt.show()


def main():

    draw_htree(0, 0, 100, 3)
    plt.show()


if __name__ == '__main__':
    main()
