# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root: #base
            return 0
        
        sum = 0

        # check if root in range, and add if so
        if low <= root.val <= high:
            sum += root.val

        # return sum + recursive node traversal
        return sum + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        

        