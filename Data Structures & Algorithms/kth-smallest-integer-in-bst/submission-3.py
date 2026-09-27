# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #  4
    #   3     5
#   2     

# IN = LNR
#[2, 3, 4, 5] # k=4

        res = [] 
        def dfs(root):
            if not root:
                return None
            
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
    
        dfs(root)
        return res[k - 1]

            

