# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return root # base
        
        if root == val: # edge case - insert @ root
            n_root = TreeNode(val, root)
            return n_root

        current = root
        while current.left or current.right:
            if val < current.val:
                current = current.left
            else:
                current = current.right
        if val < current.val:
            current.left = TreeNode(val)
        else:
            current.right = TreeNode(val)

        return root