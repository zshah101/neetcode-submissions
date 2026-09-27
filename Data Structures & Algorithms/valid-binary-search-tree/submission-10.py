# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 5
    #  3     7
#  1     2  6   8
        def dfs(root, lower, upper):
            if not root:
                return True
            if not (lower < root.val < upper):
                return False
            
            return dfs(root.left, lower, root.val) and dfs(root.right, root.val, upper)

        return dfs(root, float("-inf"), float("inf"))
            
            

        
    
                    