"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        level = len(grid)
        root = None
        if level >= 1:
            root = self.buildTree(grid, 0, level, 0, level, level)
        return root

    def buildTree(self, grid, rs, re, cs, ce, level):
        if level == 1:
            return Node(grid[rs][cs], True, None, None, None, None)

        next_level = level // 2
        tl = self.buildTree(grid, rs, re - next_level, cs, ce - next_level, next_level)
        tr = self.buildTree(grid, rs, re - next_level, ce - next_level, ce, next_level)
        bl = self.buildTree(grid, re - next_level, re, cs, ce - next_level, next_level)
        br = self.buildTree(grid, re - next_level, re, ce - next_level, ce, next_level)

        if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf:
            if tl.val == tr.val == bl.val == br.val:
                new_node = Node(tl.val, True, None, None, None, None)
            else:
                new_node = Node(tl.val, False, tl, tr, bl, br)
        else:
            new_node = Node(tl.val, False, tl, tr, bl, br)

        return new_node