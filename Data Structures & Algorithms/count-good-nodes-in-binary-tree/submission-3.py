# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = collections.deque()

        q.append((root, -float("inf")))

        while q:
            node, max_seen = q.popleft()

            if node.val >= max_seen:
                res += 1
            if node.left:
                q.append((node.left, max(max_seen, node.val)))
            if node.right:
                q.append((node.right, max(max_seen, node.val)))
        return res        