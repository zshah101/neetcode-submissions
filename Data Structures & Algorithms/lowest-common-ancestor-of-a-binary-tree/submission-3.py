# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {root: None}
        queue = collections.deque([root])

        while q not in parent or p not in parent:
            node = queue.popleft()
            
            if node.left:
                parent[node.left] = node
                queue.append(node.left)
            if node.right:
                parent[node.right] = node
                queue.append(node.right)

        ancestors = set()
        while q:
            ancestors.add(q)
            q = parent[q]
        while p not in ancestors:
            p = parent[p]
        
        return p
            
