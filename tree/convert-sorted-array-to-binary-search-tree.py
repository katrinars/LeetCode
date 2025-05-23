# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        '''
        mid = root
        recurse on .left and .right
        '''

        if not nums:
            return 
        
        mid = (len(nums) - 1) // 2
        root = TreeNode(nums[mid])

        left = self.sortedArrayToBST(nums[:mid])
        right = self.sortedArrayToBST(nums[mid+1:])

        root.left = left
        root.right = right

        return root



            