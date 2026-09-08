from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([root]) #7, 2

        while queue:
            node = queue.popleft()
            
            node.left, node.right = node.right, node.left # 4 - 7

            if node.left:
                queue.append(node.left) #7
            
            if node.right:
                queue.append(node.right) #2
        return root 
            
                

        
        