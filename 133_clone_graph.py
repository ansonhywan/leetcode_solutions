"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        node_map = {}  # Maps old node to new copy of node

        def dfs(cur):
            if cur == None:
                return cur
            if cur in node_map:
                return node_map[cur]

            node_copy = Node(cur.val, [])
            node_map[cur] = node_copy

            for n in cur.neighbors:
                node_copy.neighbors.append(dfs(n))

            return node_copy

        return dfs(node)
