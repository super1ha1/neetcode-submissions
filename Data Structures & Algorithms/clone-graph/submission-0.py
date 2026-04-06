"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        m = {}
        def bt(node):
            if node is None:
                return node
            if node in m:
                return m[node]

            clone = Node(node.val)
            m[node] = clone
            for n in node.neighbors:
                clone.neighbors.append(bt(n))
            return clone
        
        return bt(node)
